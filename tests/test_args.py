import argparse
import unittest
import pandas
from unittest import mock
from fleet.cli import main


class TestArgs(unittest.TestCase):
    data = [
        ["TESLA", "A", 1234, 42000],
        ["BMW", "B", 4321, 39563],
        ["TESLA", "A", 2233, 25000],
        ["SEAT", "A", 56789, 48000],
        ["VW", "C", 24680, 29000],
    ]

    @mock.patch("builtins.print")
    @mock.patch("fleet.parser.Car.load_file")
    @mock.patch("argparse.ArgumentParser.parse_args",
                return_value=argparse.Namespace(
                    type="count", brand="TESLA", dealership=None, mileage=None, path="file.csv"
                ))
    def test_count_brand(self, mock_args, mock_df, mock_print):
        mock_df.return_value = pandas.DataFrame(self.data)
        main()
        mock_print.assert_called_with(2)

    @mock.patch("builtins.print")
    @mock.patch("fleet.parser.Car.load_file")
    @mock.patch("argparse.ArgumentParser.parse_args",
                return_value=argparse.Namespace(
                    type="sum", brand=None, dealership="A", mileage=None, path="file.csv"
                ))
    def test_sum_dealership(self, mock_args, mock_df, mock_print):
        mock_df.return_value = pandas.DataFrame(self.data)
        main()
        mock_print.assert_called_with(115000)
