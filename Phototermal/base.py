class video_params:
    def __init__(self, fps=30, frame_width=320, frame_height=160):
        self._fps = fps
        self._width = frame_width
        self._height = frame_height
        self._callbacks = {}

    @property
    def FramePerSecond(self):
        return self._fps

    @FramePerSecond.setter
    def FramePerSecond(self, value):
        self._fps = value
        self._notify("FramePerSecond", value)

    @property
    def Width(self):
        return self._width

    @Width.setter
    def Width(self, value):
        self._width = value
        self._notify("Width", value)

    @property
    def Height(self):
        return self._height

    @Height.setter
    def Heigth(self, value):
        self._height = value
        self._notify("Width", value)

    ## This section allow to define the events controller 
    def add_listener(self, property_name, callback):
        if property_name not in self._callbacks:
            self._callbacks[property_name] = []
        self._callbacks[property_name].append(callback)
    
    ## This section allow to define the event notifier
    def _notify(self, property_name, value):
        if property_name in self._callbacks:
            for callback in self._callbacks[property_name]:
                callback(value)

    def __str__(self):
        return f"Photothermal: Temperature={self.temperature}°C, Power={self.power}W"

""" Ejemplo de uso
def temperature_changed(new_temperature):
    print(f"Temperature changed to {new_temperature}°C")

def power_changed(new_power):
    print(f"Power changed to {new_power}W")

pt = Photothermal(temperature=30, power=100)
pt.add_listener("temperature", temperature_changed)
pt.add_listener("power", power_changed)

pt.temperature = 35
pt.power = 120

print(pt)
"""
