# -*- coding: utf-8 -*-
from distutils.core import setup
from fake_rpi import __version__

packages = \
['fake_rpi']

package_data = \
{'': ['*']}

install_requires = \
['numpy']

setup_kwargs = {
    'name': 'fake-rpi',
    'version': __version__,
    'description': 'Fake Raspberry Pi programming interfaces for development or unit testing',
    'long_description': None,
    'author': 'ycbayrak',
    'author_email': 'dev@perga.co',
    'url': 'https://github.com/Perga-Biotechnology/fake_rpi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)