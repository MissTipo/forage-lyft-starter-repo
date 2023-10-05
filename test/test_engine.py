from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
import unittest


class TestCapuletEngine(unittest.TestCase):
    def test_capulet_engine_need_service(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_capulet_engine_no_need_service(self):
        current_mileage = 30000
        last_service_mileage = 30000
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

    def test_sternman_engine_needs_service(self):
        warning_light = True
        engine = SternmanEngine(warning_light)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_no_need_service(self):
        warning_light = False
        engine = SternmanEngine(warning_light)
        self.assertFalse(engine.needs_service())

    def test_willoughby_engine_needs_service(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_no_need_service(self):
        current_mileage = 60000
        last_service_mileage = 60000
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main(verbosity=2)
