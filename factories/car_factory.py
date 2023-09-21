"""Abstract Factory Class."""

from abc import ABC, abstractmethod


class CarFactory(ABC):
    """Abstract Factory Class."""

    @abstractmethod
    def create_car(self, current_date, service_date, current_mileage, last_service_mileage):
        pass


""""
    @abstractmethod
    def create_calliope(self, current_date, service_date, currrent_mileage, last_service_mileage):
        pass

    @abstractmethod
    def create_glissade(self, current_date, service_date, currrent_mileage, last_service_mileage):
        pass

    @abstractmethod
    def create_palindrome(self, current_date, service_date, currrent_mileage, last_service_mileage):
        pass

    @abstractmethod
    def create_rorschach(self, current_date, service_date, currrent_mileage, last_service_mileage):
        pass

    @abstractmethod
    def create_thovex(self, current_date, service_date, currrent_mileage, last_service_mileage):
        pass
        """
