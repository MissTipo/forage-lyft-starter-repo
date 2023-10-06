"""Octoprime tire servicing criteria."""

from tires.tires import Tires


class OctoprimeTires(Tires):
    """Octoprime tire servicing criteria."""

    def __init__(self, tire_wear_sensor):
        self.tire_wear_sensor = tire_wear_sensor

    def needs_service(self):
        """Return True if Octoprime needs servicing."""
        if sum(self.tire_wear_sensor) >= 3:
            return True
