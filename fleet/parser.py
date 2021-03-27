import pandas


class Car:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = self.load_file()
        self.df.columns = ["BRANDS", "DEALERSHIPS", "KMs", "PRICES"]

    def load_file(self):
        try:
            return pandas.read_csv(self.file_path, header=None)
        except FileNotFoundError:
            raise SystemExit("[ERROR] File does not exist. Try again.")

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
