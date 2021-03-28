from fleet.parser import Car


class CarInterface:

    def __init__(self, path):
        self.car = Car(path)

    def count(self, kind: str, value):
        dataframe = self.car.filter(kind.upper(), value)
        count = self.car.count(dataframe, kind.upper())
        return f"{count} item(s)" if count > 0 else "No item found"

    def filter(self, kind: str, value):
        if self.valid_range(value):
            dataframe = self.car.filter_in_range(kind.upper(), value)
        else:
            dataframe = self.car.filter(kind.upper(), value)
        count = self.car.count(dataframe, kind.upper())
        return dataframe.to_string(index=False) if count > 0 else "No item found"

    def sum_prices(self, kind: str, value):
        if self.valid_range(value):
            dataframe = self.car.filter_in_range(kind.upper(), value)
        else:
            dataframe = self.car.filter(kind.upper(), value)
        count = self.car.count(dataframe, kind.upper())
        return f"{'{:20,.2f}'.format(self.car.sum_prices(dataframe)).strip()} EUR" if count > 0 else "No item found"

    def report(self, kind: str, value):
        if self.valid_range(value):
            dataframe = self.car.filter_in_range(kind.upper(), value)
        else:
            dataframe = self.car.filter(kind.upper(), value)

        if self.car.count(dataframe, kind.upper()) > 0:
            response = dataframe.to_string(index=False)
            response += f"\n\nTotal: {self.car.count(dataframe, kind.upper())} item(s)"
            return response
        return "No item found"

    def valid_range(self, value):
        if type(value) == list:
            try:
                min_value = int(value[0])
                max_value = int(value[1])
                if min_value > max_value:
                    raise SystemExit("[ERROR] In a range, the first value should be lower or equal the second.")
                return True
            except IndexError:
                raise SystemExit("[ERROR] Pass two numbers as ranger parameter.")
            except ValueError:
                raise SystemExit("[ERROR] In a range, both values should be a number.")
        return False
