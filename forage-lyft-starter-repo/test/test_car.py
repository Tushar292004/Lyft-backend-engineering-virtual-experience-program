import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

class Service : 
    def battery(x) :
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - x)  # x = 3
        current_mileage = 0
        last_service_mileage = 0

        return (last_service_date, current_mileage, last_service_mileage)

    def enginet(y): 
        last_service_date = datetime.today().date()
        current_mileage = y # y = 30001
        last_service_mileage = 0

        return (last_service_date, current_mileage, last_service_mileage)

    def battery2(x):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - x)
        warning_light_is_on = False

    def engine2(y):
        last_service_date = datetime.today().date()
        warning_light_is_on = y



class TestCalliope(unittest.TestCase, Service):
    def test_battery_should_be_serviced(self):
        car = Calliope(battery(3))
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car = Calliope(battery(1))
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car = Calliope(enginet(30001))
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = Calliope(enginet(30000))
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase, Service):
    def test_battery_should_be_serviced(self):
        car = Glissade(battery(3))
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self): 
        car = Glissade(battery(1))
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car = Glissade(enginet(60001))
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = Glissade(enginet(6000))
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase, Service):
    def test_battery_should_be_serviced(self):
        car = Palindrome(battery2(5))
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car = Palindrome(battery2(3))
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car = Palindrome(engine2(True))
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = Palindrome(engine2(False))
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase, Service):
    def test_battery_should_be_serviced(self):
        car = Rorschach(battery(5))
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car = Rorschach(battery(3))
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car = Rorschach(enginet(60001))
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = Rorschach(enginet(60000))
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase, Service):
    def test_battery_should_be_serviced(self):
        car = Thovex(battery(5))
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car = Thovex(battery(3))
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car = Thovex(enginet(30001))
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = Thovex(enginet(30000))
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()


