from ..car_factory import CarFactory
from ..engine.capulet_engine import CapuletEngine
from ..battery.nubbin_battery import NubbinBattery
from ..car import Car


class Thovex(CarFactory):
    """Class Thovex."""

    def create_car(self, current_date, last_service_date, current_mileage, last_service_mileage):
        """Create a thovex car."""
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
