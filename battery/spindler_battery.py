"""A class for the Spindler battery."""

from battery.battery import Battery


class SpindlerBattery(Battery):
    """A class for the Spindler battery."""

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        """Return True if the battery needs service."""
        return (self.current_date.year - self.last_service_date.year) >= 3
