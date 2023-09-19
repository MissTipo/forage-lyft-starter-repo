"""Module calliope."""

from ..components.car import Car


class Calliope(Car):
    """Class Calliope."""

    def __init__(self, current_mileage, last_service_mileage, engine, battery):
        """Initialize class Calliope."""
        super().__init__(engine, battery)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        """Return a boolean value indicating whether a car needs service."""
        return self.engine.needs_service() or self.battery.needs_service() or (
            self.current_mileage - self.last_service_mileage > 30000
        )
