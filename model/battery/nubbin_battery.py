"""A class for the Nubbin battery."""

from battery import Battery
from datetime import date


class NubbinBattery(Battery):
    """A class for the Nubbin battery."""

    def __init__(self, last_service_date: date, current_date: date):
        """Initialize the NubbinBattery class."""
        self.last_service_date = last_service_date
        self.current_date = current_date

    def need_service(self) -> bool:
        return (self.current_date.year - self.last_service_date.year) >= 4
