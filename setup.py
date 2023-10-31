from setuptools import setup
from setuptools.command.install import install


__version__ = "0.1.0"

setup(
    name="oldplotlib",
    version=__version__,
    install_requires=["matplotlib>=3.0.0"],
    packages=["oldplotlib"],
    include_package_data=True,
    package_data={
        "oldplotlib": ["styles/*.mplstyle"],
    },
)
