import setuptools
setuptools.setup(
    name="fleet",
    version="1.0",
    author="Felipe Carvalho",
    description="Fleet reads data from a file to return a computed feedback",
    packages=setuptools.find_packages(),
    install_requires=[
        "setuptools",
        "pandas==1.2.3",
        "numpy==1.20.1"
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": ["fleet=fleet.cli:main"],
    },
)
