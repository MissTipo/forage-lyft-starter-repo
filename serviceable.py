"""Implements the Serviceable interface."""
from abc import ABC, abstractmethod, abstractmethod


class Serviceable(ABC):
    """Represent a serviceable object."""

    @abstractmethod
    def needs_service(self) -> bool:
        """Return a boolean value indicating whether the car needs service."""
        pass
