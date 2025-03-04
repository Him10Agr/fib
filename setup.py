from setuptools import find_packages, setup

setup(
    name="fib.py",
    version="0.0.1",
    author="Himanshu Agrawal",
    author_email="himanshuagr.c2@gmail.com",
    description="Calculates the fibonacci number",
    long_description="A basic library that \
                    calculates Fibonacci numbers",
    long_description_content_type="text/markdown",
    url="https://github.com/Him10Agr/fib",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independant",
    ],
    python_requires=">=3",
    tests_require = ['pytest'],
)