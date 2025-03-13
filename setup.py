from setuptools import find_packages, setup
import pathlib

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(str(pathlib.Path(__file__).parent.absolute()) + "fib/version.py", "r") as fh:
    version = fh.read().split("=")[1].replace("'", "")

setup(
    name="fib_him10agr.py",
    version=version,
    author="Himanshu Agrawal",
    author_email="himanshuagr.c2@gmail.com",
    description="Calculates the fibonacci number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Him10Agr/fib",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
    tests_require = ['pytest'],

    entry_points={
        "console_scripts": [
            'fib-number = fib_py.cmd.fib_numb:fib_numb', 
        ],
    },
)