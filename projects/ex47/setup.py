try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "Api One",
    "author": "Tomas Salazar",
    "url": "atomsfat.github",
    "download_url": "some",
    "author_emai": "my_email",
    "version": "0.1",
    "install_requires": ["nose"],
    "packages": ["EX47"],
    "scripts": [],
    "name": "api One"
    }

setup(**config)
