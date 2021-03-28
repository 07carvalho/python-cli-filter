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
                    type="count", kind="brand", value="TESLA", path="file.csv"
                ))
    def test_count_brand(self, mock_args, mock_df, mock_print):
        mock_df.return_value = pandas.DataFrame(self.data)
        main()
        mock_print.assert_called_with("2 item(s)")

    @mock.patch("builtins.print")
    @mock.patch("fleet.parser.Car.load_file")
    @mock.patch("argparse.ArgumentParser.parse_args",
                return_value=argparse.Namespace(
                    type="count", kind="brand", value="FORD", path="file.csv"
                ))
    def test_count_non_existing_brand(self, mock_args, mock_df, mock_print):
        mock_df.return_value = pandas.DataFrame(self.data)
        main()
        mock_print.assert_called_with("No item found")

    @mock.patch("builtins.print")
    @mock.patch("fleet.parser.Car.load_file")
    @mock.patch("argparse.ArgumentParser.parse_args",
                return_value=argparse.Namespace(
                    type="list", kind="brand", value="TESLA", path="file.csv"
                ))
    def test_list_brand(self, mock_args, mock_df, mock_print):
        mock_df.return_value = pandas.DataFrame(self.data)
        main()
        mock_print.assert_called_with("BRAND DEALERSHIP  MILEAGE  PRICE\nTESLA          A     1234  42000\nTESLA          A     2233  25000")

    @mock.patch("builtins.print")
    @mock.patch("fleet.parser.Car.load_file")
    @mock.patch("argparse.ArgumentParser.parse_args",
                return_value=argparse.Namespace(
                    type="price", kind="dealership", value="A", path="file.csv"
                ))
    def test_price_dealership(self, mock_args, mock_df, mock_print):
        mock_df.return_value = pandas.DataFrame(self.data)
        main()
        mock_print.assert_called_with("115,000.00 EUR")

    @mock.patch("builtins.print")
    @mock.patch("fleet.parser.Car.load_file")
    @mock.patch("argparse.ArgumentParser.parse_args",
                return_value=argparse.Namespace(
                    type="report", kind="brand", value="TESLA", path="file.csv"
                ))
    def test_report_brand(self, mock_args, mock_df, mock_print):
        mock_df.return_value = pandas.DataFrame(self.data)
        main()
        mock_print.assert_called_with("BRAND DEALERSHIP  MILEAGE  PRICE\nTESLA          A     1234  42000\nTESLA          A     2233  25000\n\nTotal: 2 item(s)")

    @mock.patch("builtins.print")
    @mock.patch("fleet.parser.Car.load_file")
    @mock.patch("argparse.ArgumentParser.parse_args",
                return_value=argparse.Namespace(
                    type="report", kind="mileage", value=None, range=[4000, 5000], path="file.csv"
                ))
    def test_report_mileage_in_range(self, mock_args, mock_df, mock_print):
        mock_df.return_value = pandas.DataFrame(self.data)
        main()
        mock_print.assert_called_with("BRAND DEALERSHIP  MILEAGE  PRICE\n  BMW          B     4321  39563\n\nTotal: 1 item(s)")

    @mock.patch("builtins.print")
    @mock.patch("fleet.parser.Car.load_file")
    @mock.patch("argparse.ArgumentParser.parse_args",
                return_value=argparse.Namespace(
                    type="collect", kind="brand", value="TESLA", path="file.csv"
                ))
    def test_wrong_type(self, mock_args, mock_df, mock_print):
        mock_df.return_value = pandas.DataFrame(self.data)
        main()
        mock_print.assert_called_with("[ERROR] Type should be \"count\", \"list\", \"price\" or \"report\"\nTry \"fleet --help\" for more information.")

    @mock.patch("builtins.print")
    @mock.patch("fleet.parser.Car.load_file")
    @mock.patch("argparse.ArgumentParser.parse_args",
                return_value=argparse.Namespace(
                    type="list", kind="brands", value="TESLA", path="file.csv"
                ))
    def test_non_existing_kind(self, mock_args, mock_df, mock_print):
        mock_df.return_value = pandas.DataFrame(self.data)
        with self.assertRaises(SystemExit) as context:
            main()
            mock_print.assert_called_with("[ERROR] Kind \"BRANDS\" does not exist. Fix and try again.")

    @mock.patch("builtins.print")
    @mock.patch("fleet.parser.Car.load_file")
    @mock.patch("argparse.ArgumentParser.parse_args",
                return_value=argparse.Namespace(
                    type="list", kind="brands", value=None, range=None, path="file.csv"
                ))
    def test_missing_option(self, mock_args, mock_df, mock_print):
        mock_df.return_value = pandas.DataFrame(self.data)
        main()
        mock_print.assert_called_with("[ERROR] Invalid options\nTry \"fleet --help\" for more information.")

    @mock.patch("builtins.print")
    @mock.patch("fleet.parser.Car.load_file")
    @mock.patch("argparse.ArgumentParser.parse_args",
                return_value=argparse.Namespace(
                    type="count", kind="brand", value="FORD", path="file.txt"
                ))
    def test_wrong_file(self, mock_args, mock_df, mock_print):
        mock_df.return_value = pandas.DataFrame(self.data)
        with self.assertRaises(SystemExit) as context:
            main()
            mock_print.assert_called_with("[ERROR] File should be a .csv")

    @mock.patch("builtins.print")
    @mock.patch("fleet.parser.Car.load_file")
    @mock.patch("argparse.ArgumentParser.parse_args",
                return_value=argparse.Namespace(
                    type="report", kind="mileage", value=None, range=[4000], path="file.csv"
                ))
    def test_report_missing_number_in_range(self, mock_args, mock_df, mock_print):
        mock_df.return_value = pandas.DataFrame(self.data)
        with self.assertRaises(ValueError) as context:
            main()
            mock_print.assert_called_with("[ERROR] In a range, both values should be a number.")

    @mock.patch("builtins.print")
    @mock.patch("fleet.parser.Car.load_file")
    @mock.patch("argparse.ArgumentParser.parse_args",
                return_value=argparse.Namespace(
                    type="report", kind="mileage", value=None, range=[4000, "two"], path="file.csv"
                ))
    def test_report_string_in_range(self, mock_args, mock_df, mock_print):
        mock_df.return_value = pandas.DataFrame(self.data)
        with self.assertRaises(SystemExit) as context:
            main()
            mock_print.assert_called_with("[ERROR] In a range, both values should be a number.")

    @mock.patch("builtins.print")
    @mock.patch("fleet.parser.Car.load_file")
    @mock.patch("argparse.ArgumentParser.parse_args",
                return_value=argparse.Namespace(
                    type="report", kind="mileage", value=None, range=[4000, 1000], path="file.csv"
                ))
    def test_report_first_number_higher_in_range(self, mock_args, mock_df, mock_print):
        mock_df.return_value = pandas.DataFrame(self.data)
        with self.assertRaises(SystemExit) as context:
            main()
            mock_print.assert_called_with("[ERROR] In a range, the first value should be lower or equal the second.")
