from ewelink_api.device import *

from ewelink_api.custom_types.devices import Devices

from logging_config import logger


def instantiate_devices(devicesData):
    devices = []
    for deviceData in devicesData:
        device = instantiate_device(deviceData)
        if device is not None:
            devices.append(device)

    return devices


def instantiate_device(deviceData):
    model = deviceData["productModel"]

    if model in Devices.CAMERA:
        return CameraDevice(**deviceData)
    elif model in Devices.THERMOSTAT:
        return ThermostatDevice(**deviceData)
    elif model in Devices.SOIL_MOISTURE:
        return SoilMoistureDevice(**deviceData)
    elif model in Devices.SMART_PLUG:
        return SmartPlugDevice(**deviceData)
    elif model in Devices.SMART_LIGHT:
        return SmartLightDevice(**deviceData)
    elif model in Devices.SMART_SWITCH:
        return SmartSwitchDevice(**deviceData)
    elif model in Devices.CONTROL_PANEL:
        return ControlPanelDevice(**deviceData)
    else:
        logger.warn("Unsupported or Invalid device model: ", deviceData)
