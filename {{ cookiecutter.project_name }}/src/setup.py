from setuptools import setup

setup(
    name="{{ cookiecutter.service_name }}",
    version="{{ cookiecutter.version }}",
    packages=["{{ cookiecutter.service_name }}"],
)
