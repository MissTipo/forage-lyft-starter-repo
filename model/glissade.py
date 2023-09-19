from ...car import Car


class Glissade(Car):
    """A."""

    def __init__(self, engine, battery, current_mileage, last_service_mileage):
        """Initialize a Glissade car."""
        super().__init__(engine, battery)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        """Return a boolean value if the car needs service."""
        return self.engine.needs_service or self.battery.needs_service or (
            self.current_mileage - self.last_service_mileage >= 60000
        )
