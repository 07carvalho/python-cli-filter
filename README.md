# fleet

A Command Line Interface (CLI) made with Python.

## About this project

#### FAQ
**What are the requirements?**

This project was developed and tested in the following requirements:
* Python 3.8
* Pandas 1.2.3

**Why Python?**

Python fulfills all the requirements for this project: has a built-in module to works with CLI, a powerful lib to read and analyse data, enable to create a portable and functional package in few hours. Python is a popular language in this scenario of data analysing.

**Why Pandas?**

Pandas is a very used open source lib in Data Science field. In this scenario, Pandas allows writing powerful and maintainable code in few lines - avoiding many for loops, for example. Pandas is also very efficient with small data (usually from 100MB up to 1GB) and performance is rarely a concern.

**It is very flexible, right?**

Yes! It is possible to apply commands to all file columns and extract valuable data. 

**How to work in a production environment?**

Once this package is published, it can be downloaded with:
> pip install git+ssh://git@github.com/07carvalho/python-cli-filter#egg=fleet


## Installation
This project can be installed via PIP as said above, or downloading this repo and running:
> python setup.py install


## Documentation

#### NAME
**fleet** - reads data from a file to return a computed feedback

#### SYNOPSIS
```
fleet [--version] [--help] <command> [<args>]
```

#### DESCRIPTION
Fleet can be used to extract valued information about a fleet from well-structured csv file. The csv file should not have a header and should have four columns in the following order: brand, dealership, mileage and price.    

#### OPTIONS
```
-V, --version
    prints the version that the program came from.
```

#### COMMANDS
```
count [options]
    count items according to the options

list [options]
    list items according to the options

price [options]
    sum car's price according to the options

report [options]
    shows a list and count itens according to the options

-k, --kind <BRAND | DEALERSHIP | MILEAGE | PRICE>
    the kind of value the user wants to compute

-v, --value <value>
    the value used to query the file

-R, --range <min, max>
    a range of minimum and maximum values to query the file

-p, --path <path>
    the path to the file to be read
```

#### EXAMPLES
Examples of commands related to brands
```
fleet count --kind brand --value TESLA --path file.csv
fleet list --kind brand --value TESLA --path file.csv
fleet price --kind brand --value TESLA --path file.csv
fleet report --kind brand --value TESLA --path file.csv
```

Examples of commands related to dealership
```
fleet count --kind dealership --value "Auto Jamor" --path file.csv
fleet list --kind dealership --value "Auto Jamor" --path file.csv
fleet price --kind dealership --value "Auto Jamor" --path file.csv
fleet report --kind dealership --value "Auto Jamor" --path file.csv
```

Examples of commands related to mileage
```
fleet count --kind mileage --value 7274 --path file.csv
fleet list --kind mileage --value 7274 --path file.csv
fleet list --kind mileage --range 7000 10000 --path file.csv
fleet report --kind mileage -R 7000 10000 --path file.csv
```

Examples of commands related to price
```
fleet count --kind price --value 43388 --path file.csv
fleet list --kind price --value 43388 --path file.csv
fleet list --kind price --range 43000 45000 --path file.csv
fleet report --kind price -R 43000 45000 --path file.csv
```


## Tests
> python3 -m unittest
