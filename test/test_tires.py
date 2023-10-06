import unittest

from tires.carrigan import CarriganTires
from tires.octoprimes import OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_carrigan_needs_service(self):
        tire_wear_sensor = [0.1, 0.4, 0.6, 0.9]
        tire = CarriganTires(tire_wear_sensor)
        self.assertTrue(tire.needs_service())

    def test_carrigan_does_not_need_service(self):
        tire_wear_sensor = [0.1, 0.4, 0.6, 0.8]
        tire = CarriganTires(tire_wear_sensor)
        self.assertFalse(tire.needs_service())


class TestOctoprimeTires(unittest.TestCase):
    def test_octoprimes_needs_service(self):
        tire_wear_sensor = [0.6, 0.8, 0.8, 0.9]
        tire = OctoprimeTires(tire_wear_sensor)
        self.assertTrue(tire.needs_service())

    def test_octoprimes_does_not_need_service(self):
        tire_wear_sensor = [0.1, 0.4, 0.6, 0.8]
        tire = OctoprimeTires(tire_wear_sensor)
        self.assertFalse(tire.needs_service())
