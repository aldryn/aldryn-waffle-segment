# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from aldryn_waffle_segment import __version__


setup(
    name='aldryn-waffle-segment',
    version=__version__,
    description=open('README.rst').read(),
    author='Divio AG',
    author_email='info@divio.com',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=[
        'django-cms',
        'aldryn-segmentation',
        'django-waffle',
    ],
    include_package_data=True,
    zip_safe=False,
)
