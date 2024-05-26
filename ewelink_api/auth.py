from ewelink_api.custom_types.region import Region

from datetime import datetime
import requests
import base64
import hmac
import hashlib
import json
from typing import Final
from email_validator import validate_email
from logging_config import logger

from ewelink_api.utils import make_nonce

# TODO: Caching of the credentials


class Auth:
    def __init__(
        self, email: str, password: str, region: str, app_id: str, app_secret: str
    ):
        self.app_id: str = app_id
        self.app_secret: str = app_secret
        self.email: str = email
        self.password: str = password
        self.region: Region = region

        self.api_url: str = f"https://{self.region}-api.coolkit.cc:8080/api"

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        validate_email(email)

        self._email = email

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str) -> None:
        self._password = password

    def getRegion(self):
        raise NotImplementedError

    def login(self) -> dict[str]:
        body: dict[str] = {
            "appid": self.app_id,
            "email": self.email,
            "phoneNumber": None,
            "password": self.password,
            "ts": int(datetime.timestamp(datetime.now())),
            "version": 8,
            "nonce": make_nonce(),
        }
        sign: Final = f"Sign {self.make_sign(self.app_secret, json.dumps(body))}"

        req: requests.models.Response = requests.post(
            f"{self.api_url}/user/login",
            headers={"Authorization": sign, "Content-Type": "application/json"},
            json=body,
        )

        res: dict = req.json()

        error = res.get("error", None)

        if error == 401:
            logger.error("Invalid email or password")
            raise ValueError("Invalid email or password")

        return {"at": res["at"], "apikey": res["user"]["apikey"]}

    def auth(self, token):
        if token is None:
            self.login()

    def make_sign(self, key: str, message: str) -> str:
        return (
            base64.b64encode(
                hmac.new(
                    key.encode(), message.encode(), digestmod=hashlib.sha256
                ).digest()
            )
        ).decode()
