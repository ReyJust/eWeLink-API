from .camera import CameraDevice
from .thermostat import ThermostatDevice
from .soil_moisture import SoilMoistureDevice
from .smart_plug import SmartPlugDevice
from .smart_light import SmartLightDevice
from .smart_switch import SmartSwitchDevice
from .control_panel import ControlPanelDevice

__all__ = [
    "CameraDevice",
    "ControlPanelDevice",
    "ThermostatDevice",
    "SoilMoistureDevice",
    "SmartPlugDevice",
    "SmartLightDevice",
    "SmartSwitchDevice",
]
