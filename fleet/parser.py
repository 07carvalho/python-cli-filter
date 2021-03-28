import pandas
from pandas.core.frame import DataFrame


class Car:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = self.load_file()
        self.df.columns = ["BRAND", "DEALERSHIP", "MILEAGE", "PRICE"]

    def load_file(self):
        try:
            return pandas.read_csv(self.file_path, header=None)
        except FileNotFoundError:
            raise SystemExit("[ERROR] File does not exist. Fix and try again.")

    def count(self, dataframe: DataFrame, column: str) -> int:
        """count number of occurrences in a column"""
        return dataframe[column].size

    def filter(self, column: str, query: str):
        """list according to query"""
        query = int(query) if query.isnumeric() else query
        try:
            return self.df[(self.df[column] == query)]
        except KeyError:
            raise SystemExit(f"[ERROR] Kind \"{column}\" does not exist. Fix and try again.")

    def filter_in_range(self, column: str, query_range):
        """list according to range"""
        try:
            return self.df[(self.df[column] >= query_range[0]) & (self.df[column] <= query_range[1])]
        except KeyError:
            raise SystemExit(f"[ERROR] Kind \"{column}\" does not exist. Fix and try again.")

    def sum_prices(self, dataframe: DataFrame) -> int:
        """get the total value of cars that exist in a given dataframe"""
        return dataframe[["PRICE"]].sum().values[0]
