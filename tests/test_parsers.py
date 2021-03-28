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
        dataframe = Car("file.csv").filter("BRAND", "TESLA")
        self.assertEqual(2, Car("file.csv").count(dataframe, "BRAND"))
        dataframe = Car("file.csv").filter("BRAND", "Tesla")
        self.assertEqual(0, Car("file.csv").count(dataframe, "BRAND"))
        dataframe = Car("file.csv").filter("BRAND", "VW")
        self.assertEqual(1, Car("file.csv").count(dataframe, "BRAND"))
        dataframe = Car("file.csv").filter("BRAND", "FORD")
        self.assertEqual(0, Car("file.csv").count(dataframe, "BRAND"))

    @mock.patch("fleet.parser.Car.load_file")
    def test_filter(self, load_file):
        load_file.return_value = pandas.DataFrame(self.data)
        self.assertEqual(2, Car("file.csv").filter("BRAND", "TESLA")["BRAND"].size)
        self.assertEqual(0, Car("file.csv").filter("BRAND", "Tesla")["BRAND"].size)
        self.assertEqual(1, Car("file.csv").filter("BRAND", "VW")["BRAND"].size)
        self.assertEqual(0, Car("file.csv").filter("BRAND", "FORD")["BRAND"].size)

    @mock.patch("fleet.parser.Car.load_file")
    def test_filter_in_range(self, load_file):
        load_file.return_value = pandas.DataFrame(self.data)
        self.assertEqual(2, Car("file.csv").filter_in_range("MILEAGE", [1200, 3000])["BRAND"].size)
        self.assertEqual(1, Car("file.csv").filter_in_range("MILEAGE", [24000, 30000])["BRAND"].size)
        self.assertEqual(0, Car("file.csv").filter_in_range("MILEAGE", [0, 1000])["BRAND"].size)

    @mock.patch("fleet.parser.Car.load_file")
    def test_sum_prices(self, load_file):
        load_file.return_value = pandas.DataFrame(self.data)
        dataframe = Car("file.csv").filter("DEALERSHIP", "A")
        self.assertEqual(115000, Car("file.csv").sum_prices(dataframe))
        dataframe = Car("file.csv").filter("DEALERSHIP", "B")
        self.assertEqual(39563, Car("file.csv").sum_prices(dataframe))
        dataframe = Car("file.csv").filter("DEALERSHIP", "C")
        self.assertEqual(29000, Car("file.csv").sum_prices(dataframe))
        dataframe = Car("file.csv").filter("DEALERSHIP", "Z")
        self.assertEqual(0, Car("file.csv").sum_prices(dataframe))
