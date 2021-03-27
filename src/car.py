import pandas


class Car:
    file_path = "data/backend_file-calculation_dealership.csv"

    def __init__(self):
        self.df = self.load_file()
        self.df.columns = ["BRANDS", "DEALERSHIPS", "KMs", "PRICE"]

    def load_file(self):
        return pandas.read_csv(self.file_path, header=None)

    def count_cars_by_brand(self, brand: str) -> int:
        """get the number of cars by brand"""
        return self.df[(self.df["BRANDS"] == brand)]["BRANDS"].size

    def list_cars_by_brand(self, brand: str):
        """get list of cars by brand"""
        return self.df[(self.df["BRANDS"] == brand)] # [["DEALERSHIPS", "KMs", "PRICE"]]

    def list_cars_by_mileage_range(self, min_mileage: int, max_mileage: int):
        """get list of cars by mileage range"""
        return self.df[(self.df["KMs"] >= min_mileage) & (self.df["KMs"] <= max_mileage)] # [["DEALERSHIPS", "KMs", "PRICE"]]

    def sum_prices_by_dealership(self, dealership: str) -> int:
        """get the total value of cars that exist in a given dealership"""
        return self.df[(self.df["DEALERSHIPS"] == dealership)][["PRICE"]].sum().values[0]
