from fleet.parser import Car


class CarController:
    def __init__(self):
        self.car = Car()

    def count(self, column: str, query: str):
        filtered = self.car.filter({column: query})
        return self.car.count()

    def list_cars_by_brand(self):
        return Car().list_cars_by_brand(self.arg)

    def list_cars_by_mileage_range(self):
        return Car().list_cars_by_mileage_range(self.arg)

    def sum_prices_by_dealership(self):
        return Car().sum_prices_by_dealership(self.arg)