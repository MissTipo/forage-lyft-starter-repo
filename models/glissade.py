from ..car_factory import CarFactory
from ..engine.willoughby_engine import WilloughbyEngine
from ..battery.spindler_battery import SpindlerBattery
from ..car import Car


class Glissade(CarFactory):
    """class Glissade."""

    def create_car(self, current_date, last_service_date, current_mileage, last_service_mileage):
        """Create a glissade car."""
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
