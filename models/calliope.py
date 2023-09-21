"""Module calliope."""

from ..car_factory import CarFactory
from ..engine.capulet_engine import CapuletEngine
from ..battery.spindler_battery import SpindlerBattery
from ..car import Car


class Calliope(CarFactory):
    """Class Calliope."""

    def create_car(self, current_date, last_service_date, current_mileage, last_service_mileage):
        """Create a calliope car."""
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
