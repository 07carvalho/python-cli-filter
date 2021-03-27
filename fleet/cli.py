import argparse
from fleet.parser import Car


def main():
    parser = argparse.ArgumentParser(
        description="Reads data from a file to return a computed feedback.",
    )
    parser.version = "1.0"
    parser.add_argument("-b",
                        "--brand",
                        action="store",
                        type=str,
                        help="car's brand")
    parser.add_argument("-m",
                        "--mileage",
                        action="store",
                        type=int,
                        nargs=2,
                        metavar=("min", "max"),
                        help="mileage range")
    parser.add_argument("-d",
                        "--dealership",
                        action="store",
                        type=str,
                        help="dealership's name")
    parser.add_argument("type",
                        action="store",
                        type=str,
                        help="count or list")
    parser.add_argument("-v",
                        "--version",
                        action='version')

    args = parser.parse_args()
    print(args)
    if args.type == "count" and args.brand:
        print(Car().count("BRANDS", args.brand))
    elif args.brand and args.type == "list":
        print(Car().filter("BRANDS", args.brand))
    elif args.mileage and args.type == "list":
        print(Car().filter_in_range("KMs", args.mileage))
    elif args.dealership and args.type == "count":
        print(Car().filter_and_sum("DEALERSHIPS", "PRICES", args.dealership))
    else:
        print("error: invalid option\ntry \"python3 filter.py --help\" for more information.")
