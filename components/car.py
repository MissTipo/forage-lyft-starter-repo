"""Car class for the car service program."""
from ..serviceable import Serviceable


class Car(Serviceable):
    """Car class for the car service program."""

    def __init__(self, engine, battery):
        """Initialise a Car object."""
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        """Return True if the car needs a service."""
        return self.engine.needs_service() or self.battery.needs_service()
