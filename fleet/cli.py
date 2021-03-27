import argparse
from fleet.parser import Car


def controller(args):
    if args.type is not None and args.type in ["count", "list", "report", "sum"]:
        if not args.path.endswith(".csv"):
            raise SystemExit("[ERROR] File should be a .csv")
        car = Car(args.path)
        if args.type == "count" and args.brand:
            print(car.count("BRANDS", args.brand))
        elif args.brand and args.type == "list":
            print(car.filter("BRANDS", args.brand))
        elif args.mileage and args.type == "list":
            print(car.filter_in_range("KMs", args.mileage))
        elif args.dealership and args.type == "sum":
            print(car.filter_and_sum("DEALERSHIPS", "PRICES", args.dealership))
        else:
            print("error: invalid option\ntry \"fleet --help\" for more information.")
    else:
        print("error: type should be \"count\", \"list\", \"report\" or \"sum\"\ntry \"fleet --help\" for more information.")


def main():
    parser = argparse.ArgumentParser(
        description="Reads data from a file to return a computed feedback.",
    )
    parser.version = "1.0"
    parser.add_argument(
        "-b",
        "--brand",
        action="store",
        type=str,
        help="car's brand"
    )
    parser.add_argument(
        "-m",
        "--mileage",
        action="store",
        type=int,
        nargs=2,
        metavar=("min", "max"),
        help="mileage range",
    )
    parser.add_argument(
        "-d",
        "--dealership",
        action="store",
        type=str,
        help="dealership's name"
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
        help="count (return quantity), list (shows a list), sum (total values), and report (shows a list and quantity of elements)",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version"
    )

    controller(parser.parse_args())
