import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "jsondb",
    version = "0.1.1",
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", 'tests.py', "*tests*"] ),

    # metadata for upload to PyPI
    author = "Paul Munday",
    author_email = "contactme@paulmunday.net",
    description = "Python module that loads a dictionary from a json file and allows you to access it as a simple nosql db like key value store. Heavily influenced by PickleDB.",
    license = "GPL",
    keywords = "json db key value store",
    # could also include long_description, download_url, classifiers, etc.
)
