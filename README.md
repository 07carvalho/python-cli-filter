# python-cli-filter

A Command Line Interface (CLI) made with Python.

## About this project

#### FAQ
**What are the requirements?**
* Python 3.8, once this project was developed and tested only with this version yet.
* Pandas 1.2.3

**Why Python?**

Python fulfills all the requirements for this project: has a built-in module to works with CLI, a powerful lib to read and analyse data, enable to create a portable and functional package in few hours. Python is a popular language in this scenario of data analysing.

**Why Pandas?**

Pandas is a very used open source lib in Data Science field. In this scenario, Pandas allows writing powerful and maintainable code in few lines - avoiding many for loops, for example. Pandas is also very efficient with small data (usually from 100MB up to 1GB) and performance is rarely a concern.


## Installation
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
--version
    prints the version that the program came from.
```

#### COMMANDS
```
count [options]
    count items according to the options in the CLI

list [options]
    list items according to the options in the CLI

sum [options]
    sum items values according to the options in the CLI

-b, --brand=BRAND
    get the number of cars by brand

-d, --dealership=DEALERSHIP
    get the number of cars by brand

-m, --mileage=MILEAGE
    get the number of cars by brand
```

#### EXAMPLES
Examples of commands related to brands
```
fleet count --brand SomeBrand
fleet list --brand SomeBrand
```

Examples of commands related to dealership
```
fleet count --dealership SomeDealership
fleet list --brand SomeBrand
```

Examples of commands related to mileage
```
fleet list --mileage minValue maxValue
```


## Tests
> python3 -m unittest
