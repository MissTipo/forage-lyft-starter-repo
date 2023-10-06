from tires.tires import Tires


class CarriganTires(Tires):
    """Carrigan class."""

    def __init__(self, tire_wear_sensor):
        self.tire_wear_sensor = tire_wear_sensor

    def needs_service(self) -> bool:
        """Return True if Carrigan needs service."""
        for i in self.tire_wear_sensor:
            if i >= 0.9:
                return True
        return False
