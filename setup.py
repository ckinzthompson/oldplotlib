import atexit
from setuptools import setup
from setuptools.command.install import install


def _post_install():
    import oldplotlib

    oldplotlib.copy_style()


class new_install(install):
    def __init__(self, *args, **kwargs):
        super(new_install, self).__init__(*args, **kwargs)
        atexit.register(_post_install)


__version__ = "0.1.0"

setup(
    name="oldplotlib",
    version=__version__,
    install_requires=["matplotlib>=3.0.0"],
    packages=["oldplotlib"],
    cmdclass={"install": new_install},
    include_package_data=True,
)
