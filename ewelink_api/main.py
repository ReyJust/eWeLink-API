# 3rd Party Imports
import requests
import json
from typing import Literal, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

# Local Imports
from logging_config import logger
from auth import Auth
from ewelink_api.custom_types.region import Region
from ewelink_api.utils import get_epoch, instantiate_devices


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    ENV: str = "dev"
    APP_ID: str
    APP_SECRET: str


class EWeLinkAPI:
    def __init__(self, email: str, password: str, region: Optional[str]) -> None:
        logger.debug("Initializing EWeLinkAPI")
        settings = Settings(_env_file=".env", _env_file_encoding="utf-8")

        self.app_id: str = settings.APP_ID
        self.app_secret: str = settings.APP_SECRET
        self.env: str = settings.ENV

        self.Auth = Auth(
            email=email,
            password=password,
            region=region,
            app_id=settings.APP_ID,
            app_secret=settings.APP_SECRET,
        )

        if region is None:
            region = self.Auth.getRegion()
        self.region: Region = region

        self.api_url: str = f"https://{self.region}-api.coolkit.cc:8080/api"

    @property
    def region(self) -> Region:
        return self._region

    @region.setter
    def region(self, region: str) -> None:

        if region not in {member.value for member in Region}:
            raise ValueError("Invalid region")

        self._region = region

    def api_request(
        self, method: Literal["GET", "POST"], uri: str, params: dict, payload=None
    ) -> dict:

        url = f"{self.api_url}/{uri}"
        credentials = self.Auth.login()

        headers: dict = {
            "Authorization": f'Bearer {credentials["at"]}',
            "Content-Type": "application/json",
        }

        try:
            req: requests.models.Response = requests.request(
                method=method, url=url, headers=headers, params=params, json=payload
            )

            res = req.json()
            if "error" in res:
                if res["error"] == 406:
                    print("Refreshing creds...")
                    return self.api_request(method, uri, params, payload)

                if req.status_code != 200:
                    raise Exception(
                        f"API CALL FAILED HTTP: {res['error']}, {json.loads(res['msg'])['msg']}"
                    )

            return res

        except Exception as err:
            raise Exception(f"[ERROR] {err}")

    def get_devices(self) -> dict:
        if self.env == "prod":
            params: dict = {
                "lang": "en",
                "appid": self.app_id,
                "ts": get_epoch(),
                "version": 8,
                "getTags": 1,
            }

            devices = self.api_request("GET", "user/device", params)
        else:
            with open("ewelink_api/example_device_list.json", "r") as f:
                devices = json.load(f)

        devices_data = devices["devicelist"]
        [device_data.pop("__v") for device_data in devices_data]

        devices_objects = instantiate_devices(devices_data)

        return {
            "count": len(devices_objects),
            "devices": devices_objects,
        }

    # def get_device(self, id: int) -> dict:

    #     params: dict = {
    #         "deviceid": id,
    #         "appid": self._APP_ID,
    #         "ts": self.get_ts(),
    #         "version": 8,
    #     }

    #     device = self.call_api("GET", f"user/device/{id}", params)

    #     return device

    # def get_device_th(self, id: int) -> dict:

    #     device: dict = self.get_device(id)
    #     sensor_values: dict = {}

    #     if "currentTemperature" in list(device["params"]):
    #         sensor_values["t"] = device["params"]["currentTemperature"]
    #         sensor_values["h"] = device["params"]["currentHumidity"]

    #         for k, v in sensor_values.items():
    #             if v != "unavailable":
    #                 v = float(v)

    #     else:
    #         raise Exception(f"{id} is not a Sensor!")

    #     return sensor_values


if __name__ == "__main__":
    sdk = EWeLinkAPI(email="", password="", region="eu")

    devices = sdk.get_devices()

    print(devices)
