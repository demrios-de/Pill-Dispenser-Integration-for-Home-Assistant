from __future__ import annotations

import asyncio
import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_HOST): str,
        vol.Optional(CONF_NAME): str,
    }
)


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    host = data[CONF_HOST].strip()
    host = host.replace("http://", "").replace("https://", "").rstrip("/")

    session = async_get_clientsession(hass)

    try:
        async with asyncio.timeout(10):
            async with session.get(f"http://{host}/api/status") as response:
                if response.status != 200:
                    async with session.get(f"http://{host}/tr_name?id=1") as legacy_resp:
                        if legacy_resp.status != 200:
                            raise ConnectionError("Cannot connect to pill dispenser")
    except Exception as err:
        raise ConnectionError(f"Cannot connect to pill dispenser: {err}") from err

    name = data.get(CONF_NAME) or f"Pill Dispenser ({host})"
    return {"title": name, "host": host, "name": name}


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)
            except ConnectionError:
                errors["base"] = "cannot_connect"
            except Exception:
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                await self.async_set_unique_id(info["host"])
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=info["title"],
                    data={
                        CONF_HOST: info["host"],
                        CONF_NAME: info["name"],
                    },
                )

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )
