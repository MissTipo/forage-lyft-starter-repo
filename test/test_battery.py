from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
import unittest
from datetime import datetime


class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_battery_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 6)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_does_not_need_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

    def test_spindler_battery_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_does_not_need_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
