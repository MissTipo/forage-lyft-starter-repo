"""A concrete  subclass of the CarFactory."""

from car_factory import CarFactory


class Cars(CarFactory):
    """A concrete subclass Cars."""

    cars = ['calliope', 'glissade', 'palindrome', 'rorschach', 'thovex']

    def create_car(self, current_date, service_date, current_mileage, last_service_mileage, engine, battery):
        for car in cars:
            car = Car(engine, battery)
            return car
