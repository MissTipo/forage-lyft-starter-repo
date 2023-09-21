"""Abstract Factory Class."""
from engine.engine import Engine
from battery.battery import Battery


from abc import ABC, abstractmethod


class CarFactory(ABC):
    """Abstract Factory Class."""

    @abstractmethod
    def create_car(self, current_date, service_date, current_mileage, last_service_mileage):
        """Abstract facrory method."""
        pass
