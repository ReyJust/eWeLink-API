from ewelink_api.device.device import Device, Params
from dataclasses import dataclass
from logging_config import logger

from typing import Dict, Any


@dataclass
class ThermostatParams(Params):
    currentHumidity: str
    currentTemperature: str


class ThermostatDevice(Device):
    def __init__(self, *args, params: Dict[str, Any], **kwargs):
        thermostat_params = ThermostatParams(**params)
        super().__init__(*args, params=thermostat_params, **kwargs)

    def get_temperature(self) -> dict:
        try:
            return float(self.params.currentTemperature)
        except ValueError:
            logger.warning(
                "Failed to convert temperature to float. "
                f"Temperature: {self.params.currentTemperature}"
            )

        return None

    def get_humidity(self):
        try:
            return float(self.params.currentHumidity)
        except ValueError:
            logger.warning(
                "Failed to convert humidity to float. "
                f"Humidity: {self.params.currentHumidity}"
            )

        return None

    def get_temperature_and_humidity(self):
        return {
            "temperature": self.get_temperature(),
            "humidity": self.get_humidity(),
        }
