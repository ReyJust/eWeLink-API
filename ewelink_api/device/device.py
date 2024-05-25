from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class Room:
    id: str


@dataclass
class Family:
    id: str
    index: int
    members: List[Any]
    room: Room


@dataclass
class ExtraDetail:
    uiid: int
    description: str
    brandId: str
    apmac: str
    mac: str
    ui: str
    modelInfo: str
    model: str
    manufacturer: str
    staMac: str


@dataclass
class Extra:
    _id: str
    extra: ExtraDetail


@dataclass
class Settings:
    opsNotify: int
    opsHistory: int
    alarmNotify: int
    wxAlarmNotify: int
    wxOpsNotify: int
    wxDoorbellNotify: int
    appDoorbellNotify: int
    offlineNotify: int


@dataclass
class BindInfos:
    ifttt: List[str]
    scene: int


@dataclass
class Params:
    bindInfos: BindInfos
    version: int
    sledOnline: str
    init: int
    switch: str
    fwVersion: str
    rssi: int
    staMac: str
    startup: str
    pulse: str
    pulseWidth: int
    deviceType: str
    mainSwitch: str
    sensorType: str
    currentHumidity: str
    currentTemperature: str
    targets: List[Dict[str, Any]]
    uiActive: int
    only_device: Dict[str, str]
    ssid: str
    bssid: str
    password: str
    timeZone: int


class Device:
    def __init__(
        self,
        _id: str,
        family: Family,
        group: str,
        online: bool,
        groups: List[Any],
        devGroups: List[Any],
        relational: List[Any],
        deviceid: str,
        name: str,
        type: str,
        apikey: str,
        extra: Extra,
        settings: Settings,
        params: Params,
        createdAt: str,
        shareUsersInfo: List[Any],
        # __v: int,
        onlineTime: str,
        ip: str,
        location: str,
        offlineTime: str,
        address: str,
        sharedTo: List[Any],
        devicekey: str,
        deviceUrl: str,
        brandName: str,
        showBrand: bool,
        brandLogoUrl: str,
        productModel: str,
        devConfig: Dict[str, Any],
        uiid: int,
        tags: Dict[str, str] = {},
        extraNotify: dict = {},
    ):
        self._id = _id
        self.family = family
        self.group = group
        self.online = online
        self.groups = groups
        self.devGroups = devGroups
        self.relational = relational
        self.deviceid = deviceid
        self.name = name
        self.type = type
        self.apikey = apikey
        self.extra = extra
        self.settings = settings
        self.params = params
        self.createdAt = createdAt
        self.shareUsersInfo = shareUsersInfo
        # self.__v = __v
        self.onlineTime = onlineTime
        self.ip = ip
        self.location = location
        self.offlineTime = offlineTime
        self.tags = tags
        self.address = address
        self.sharedTo = sharedTo
        self.devicekey = devicekey
        self.deviceUrl = deviceUrl
        self.brandName = brandName
        self.showBrand = showBrand
        self.brandLogoUrl = brandLogoUrl
        self.productModel = productModel
        self.devConfig = devConfig
        self.uiid = uiid
        self.extraNotify = extraNotify

    def get_id(self) -> str:
        return self._id

    def get_family(self) -> Family:
        return self.family

    def get_group(self) -> str:
        return self.group

    def is_online(self) -> bool:
        return self.online

    def get_groups(self) -> List[Any]:
        return self.groups

    def get_devGroups(self) -> List[Any]:
        return self.devGroups

    def get_relational(self) -> List[Any]:
        return self.relational

    def get_deviceid(self) -> str:
        return self.deviceid

    def get_name(self) -> str:
        return self.name

    def get_type(self) -> str:
        return self.type

    def get_apikey(self) -> str:
        return self.apikey

    def get_extra(self) -> Extra:
        return self.extra

    def get_settings(self) -> Settings:
        return self.settings

    def get_params(self) -> Params:
        return self.params

    def get_createdAt(self) -> str:
        return self.createdAt

    def get_shareUsersInfo(self) -> List[Any]:
        return self.shareUsersInfo

    def get_onlineTime(self) -> str:
        return self.onlineTime

    def get_ip(self) -> str:
        return self.ip

    def get_location(self) -> str:
        return self.location

    def get_offlineTime(self) -> str:
        return self.offlineTime

    def get_tags(self) -> Dict[str, str]:
        return self.tags

    def get_address(self) -> str:
        return self.address

    def get_sharedTo(self) -> List[Any]:
        return self.sharedTo

    def get_devicekey(self) -> str:
        return self.devicekey

    def get_deviceUrl(self) -> str:
        return self.deviceUrl

    def get_brandName(self) -> str:
        return self.brandName

    def is_showBrand(self) -> bool:
        return self.showBrand

    def get_brandLogoUrl(self) -> str:
        return self.brandLogoUrl

    def get_productModel(self) -> str:
        return self.productModel

    def get_devConfig(self) -> Dict[str, Any]:
        return self.devConfig

    def get_uiid(self) -> int:
        return self.uiid

    def get_identity(self) -> Dict[str, Any]:
        device_info = {
            "deviceid": self.get_deviceid(),
            "name": self.get_name(),
            "type": self.get_type(),
            "online": self.is_online(),
            "location": self.get_location(),
            "ip": self.get_ip(),
        }
        return device_info












