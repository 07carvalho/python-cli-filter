import unittest
import pandas
from unittest import mock
from src.car import Car


class TestCar(unittest.TestCase):
    data = [
        ["TESLA", "A", 1234, 42000],
        ["BMW", "B", 4321, 39563],
        ["TESLA", "A", 2233, 25000],
        ["SEAT", "A", 56789, 48000],
        ["VW", "C", 24680, 29000],
    ]

    @mock.patch("src.car.Car.load_file")
    def test_count_cars(self, load_file):
        load_file.return_value = pandas.DataFrame(self.data)
        self.assertEqual(2, Car().count_cars_by_brand("TESLA"))
        self.assertEqual(0, Car().count_cars_by_brand("Tesla"))
        self.assertEqual(1, Car().count_cars_by_brand("VW"))
        self.assertEqual(0, Car().count_cars_by_brand("FORD"))

    @mock.patch("src.car.Car.load_file")
    def test_list_cars_by_brand(self, load_file):
        load_file.return_value = pandas.DataFrame(self.data)
        self.assertEqual(2, Car().list_cars_by_brand("TESLA")["BRANDS"].size)
        self.assertEqual(0, Car().list_cars_by_brand("Tesla")["BRANDS"].size)
        self.assertEqual(1, Car().list_cars_by_brand("VW")["BRANDS"].size)
        self.assertEqual(0, Car().list_cars_by_brand("FORD")["BRANDS"].size)

    @mock.patch("src.car.Car.load_file")
    def test_list_cars_by_mileage_range(self, load_file):
        load_file.return_value = pandas.DataFrame(self.data)
        self.assertEqual(2, Car().list_cars_by_mileage_range(1200, 3000)["BRANDS"].size)
        self.assertEqual(1, Car().list_cars_by_mileage_range(24000, 30000)["BRANDS"].size)
        self.assertEqual(0, Car().list_cars_by_mileage_range(0, 1000)["BRANDS"].size)

    @mock.patch("src.car.Car.load_file")
    def test_sum_prices_by_dealership(self, load_file):
        load_file.return_value = pandas.DataFrame(self.data)
        self.assertEqual(115000, Car().sum_prices_by_dealership("A"))
        self.assertEqual(39563, Car().sum_prices_by_dealership("B"))
        self.assertEqual(29000, Car().sum_prices_by_dealership("C"))
        self.assertEqual(0, Car().sum_prices_by_dealership("Z"))


if __name__ == '__main__':
    unittest.main()
