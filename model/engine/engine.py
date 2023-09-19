"""Absttract Class for Engine."""

from ...serviceable import Serviceable


class Engine(Serviceable):
    """Abstarct class."""

    def needs_service(self):
        """Abstract method."""
        pass
