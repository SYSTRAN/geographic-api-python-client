# Systran Geographic Client Library.
This is a Python implementation of the [Systran Geographic](https://api-platform-stag.systran.net/reference/geographic) Client Library.

## Requirements.
Python 2.7 and later.

## Setuptools
You can install the bindings via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install
```

## Tests

You can run the tests in the current python platform using nosetests:

```sh
// Copy your api key into "api_key.txt" file
$ echo YOUR_API_KEY > api_key.txt
$ pip install nose
$ nosetests -v tests/
```