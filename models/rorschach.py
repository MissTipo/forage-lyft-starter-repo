from ..car_factory import CarFactory
from ..engine.willoughby_engine import WilloughbyEngine
from ..battery.nubbin_battery import NubbinBattery
from ..car import Car


class Rorschach(CarFactory):
    """A class that represents a Rorschach car factory."""

    def create_car(self, current_date, last_service_date, current_mileage, last_service_mileage):
        """Create a car with a Willoughby engine and a Nubbin battery."""
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(battery, engine)
        return car
