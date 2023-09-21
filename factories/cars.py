"""A concrete  subclass of the CarFactory."""

from car_factory import CarFactory
# from ..car import Car


class Cars(CarFactory):
    """A concrete subclass Cars."""

    cars = {'calliope': ['capulet', 'spindler'],
            'glissade': ['willoughby, spindler'],
            'palindrome': ['sternman', 'spindler'],
            'rorschach': ['willoughby', 'nubbin'],
            'thovex': ['capulet, nubbin']}

    def create_car(self, current_date, service_date, current_mileage, last_service_mileage, engine, battery):
        """Concrete creator method."""
        super().create_car(current_date, service_date,
                           current_mileage, last_service_mileage)
        for k, v in Cars.cars.items():
            if 'capulet' and 'spindler' in v:
                return k
            elif 'willoughby' and 'spindler' in v:
                return k
            elif 'sternman' and 'spindler':
                return k
            elif 'willoughby' and 'nubbin':
                return k
            elif 'capulet' and 'nubbin':
                return k

        # for car in Cars.cars:
            # car = Car(engine, battery)
            # return car
