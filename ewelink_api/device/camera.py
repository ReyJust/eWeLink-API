from ewelink_api.device.device import Device

class CameraDevice(Device):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your CameraDevice initialization code here
