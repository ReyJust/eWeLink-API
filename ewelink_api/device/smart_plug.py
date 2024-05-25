from ewelink_api.device.device import Device

class SmartPlugDevice(Device):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)