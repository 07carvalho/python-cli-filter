import argparse
from fleet.interfaces import CarInterface


def controller(args):
    if args.type is not None and args.type in ["count", "list", "price", "report"]:
        if not args.path.endswith(".csv"):
            raise SystemExit("[ERROR] File should be a .csv")

        car = CarInterface(args.path)

        if args.type == "count":
            print(car.count(args.kind, args.value))
        elif args.type == "list":
            value = args.value if args.value else args.range
            print(car.filter(args.kind, value))
        elif args.type == "price":
            value = args.value if args.value else args.range
            print(car.sum_prices(args.kind, value))
        elif args.type == "report":
            value = args.value if args.value else args.range
            print(car.report(args.kind, value))
        else:
            print("error: invalid option\ntry \"fleet --help\" for more information.")
    else:
        print("error: type should be \"count\", \"list\", \"price\" or \"report\"\ntry \"fleet --help\" for more information.")


def main():
    parser = argparse.ArgumentParser(
        description="Reads data from a file to return a computed feedback.",
    )
    parser.version = "1.0.0"
    parser.add_argument(
        "-k",
        "--kind",
        action="store",
        type=str,
        help="the kind of data (brand, dealership, mileage or price)"
    )
    parser.add_argument(
        "-v",
        "--value",
        action="store",
        type=str,
        help="value"
    )
    parser.add_argument(
        "-R",
        "--range",
        action="store",
        type=int,
        nargs=2,
        metavar=("min", "max"),
        help="mileage scope (min and max)",
    )
    parser.add_argument(
        "-p",
        "--path",
        action="store",
        type=str,
        required=True,
        help="file path"
    )
    parser.add_argument(
        "type",
        action="store",
        type=str,
        help="count (return quantity), list (shows a list), price (sum car price), and report (shows a list and quantity of elements)",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version"
    )

    controller(parser.parse_args())
