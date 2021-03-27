import unittest
import pandas
from unittest import mock
from fleet.parser import Car


class TestCarParser(unittest.TestCase):
    data = [
        ["TESLA", "A", 1234, 42000],
        ["BMW", "B", 4321, 39563],
        ["TESLA", "A", 2233, 25000],
        ["SEAT", "A", 56789, 48000],
        ["VW", "C", 24680, 29000],
    ]

    @mock.patch("fleet.parser.Car.load_file")
    def test_count(self, load_file):
        load_file.return_value = pandas.DataFrame(self.data)
        self.assertEqual(2, Car().count("BRANDS", "TESLA"))
        self.assertEqual(0, Car().count("BRANDS", "Tesla"))
        self.assertEqual(1, Car().count("BRANDS", "VW"))
        self.assertEqual(0, Car().count("BRANDS", "FORD"))

    @mock.patch("fleet.parser.Car.load_file")
    def test_filter(self, load_file):
        load_file.return_value = pandas.DataFrame(self.data)
        self.assertEqual(2, Car().filter("BRANDS", "TESLA")["BRANDS"].size)
        self.assertEqual(0, Car().filter("BRANDS", "Tesla")["BRANDS"].size)
        self.assertEqual(1, Car().filter("BRANDS", "VW")["BRANDS"].size)
        self.assertEqual(0, Car().filter("BRANDS", "FORD")["BRANDS"].size)

    @mock.patch("fleet.parser.Car.load_file")
    def test_filter_in_range(self, load_file):
        load_file.return_value = pandas.DataFrame(self.data)
        self.assertEqual(2, Car().filter_in_range("KMs", [1200, 3000])["BRANDS"].size)
        self.assertEqual(1, Car().filter_in_range("KMs", [24000, 30000])["BRANDS"].size)
        self.assertEqual(0, Car().filter_in_range("KMs", [0, 1000])["BRANDS"].size)

    @mock.patch("fleet.parser.Car.load_file")
    def test_filter_and_sum(self, load_file):
        load_file.return_value = pandas.DataFrame(self.data)
        self.assertEqual(115000, Car().filter_and_sum("DEALERSHIPS", "PRICES", "A"))
        self.assertEqual(39563, Car().filter_and_sum("DEALERSHIPS", "PRICES", "B"))
        self.assertEqual(29000, Car().filter_and_sum("DEALERSHIPS", "PRICES", "C"))
        self.assertEqual(0, Car().filter_and_sum("DEALERSHIPS", "PRICES", "Z"))


if __name__ == '__main__':
    unittest.main()
