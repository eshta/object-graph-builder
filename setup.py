import os
from codecs import open

from setuptools import setup, find_packages


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION = __import__('django_pinject').__version__


with open(os.path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='django-pinject',
    version=VERSION,
    description='Integrate pinject dependency injection container into Django.',
    long_description=long_description,
    url='https://github.com/eshta/django-pinject',
    project_urls={
        'Bug Reports': 'https://github.com/eshta/django-pinject/issues',
        'Source': 'https://github.com/eshta/django-pinject',
    },
    author='Omar Shaban',
    author_email='o.shaban.000@gmail.com',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=['pinject'],
    include_package_data=True,
    keywords='django pinject',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
