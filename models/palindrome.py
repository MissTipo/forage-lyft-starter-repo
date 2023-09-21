
from ..car_factory import CarFactory
from ..engine.sternman_engine import SternmanEngine
from ..battery.spindler_battery import SpindlerBattery
from ..car import Car


class Palindrome(CarFactory):
    """Class Palindrome."""

    def create_car(self, current_date, last_service_date, warning_light_is_on):
        """Create a palindrome car."""
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
