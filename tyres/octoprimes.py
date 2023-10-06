"""Octoprime tire servicing criteria."""

from serviceable import Serviceable


class Octoprime(Serviceable):
    """Octoprime tire servicing criteria."""

    def needs_service(self):
        """Return True if Octoprime needs servicing."""
        sensor = [0, 0.4, 0.8, 1]
        if sum(sensor) >= 3:
            return True
