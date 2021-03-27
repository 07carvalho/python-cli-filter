import pandas


class Car:
    file_path = "data/backend_file-calculation_dealership.csv"

    def __init__(self):
        self.df = self.load_file()
        self.df.columns = ["BRANDS", "DEALERSHIPS", "KMs", "PRICES"]

    def load_file(self):
        return pandas.read_csv(self.file_path, header=None)

    def count(self, column: str, query: str) -> int:
        """count number of occurrences in a column"""
        return self.df[(self.df[column] == query)][column].size

    def filter(self, column: str, query: str):
        """list according to query"""
        return self.df[(self.df[column] == query)]

    def filter_in_range(self, column: str, query_range):
        """list according to range"""
        return self.df[(self.df[column] >= query_range[0]) & (self.df[column] <= query_range[1])]

    def filter_and_sum(self, filtered_column: str, column: str, query: str) -> int:
        """get the total value of cars that exist in a given dealership"""
        return self.df[(self.df[filtered_column] == query)][[column]].sum().values[0]
