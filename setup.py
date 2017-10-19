import re
import os
import sys

from setuptools import setup

# get version without importing
with open('jeaves/__init__.py', 'rb') as f:
    VERSION = str(re.search('__version__ = \'(.+?)\'', f.read().decode('utf-8')).group(1))

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist')
    os.system('twine upload dist/django-jeaves-{}.tar.gz'.format(VERSION))
    message = '\nreleased [{version}](https://pypi.python.org/pypi/django-jeaves/{version})'
    print(message.format(version=VERSION))
    sys.exit()

if sys.argv[-1] == 'tag':
    os.system("git tag -a v{} -m 'tagging v{}'".format(VERSION, VERSION))
    os.system('git push --tags && git push origin master')
    sys.exit()


setup(
    name='django-jeaves',
    version=VERSION,
    packages=['jeaves'],
    description='Django EAV using JSONField',

    author='Dylan Verheul',
    author_email='dylan@zostera.nl',
    url='https://github.com/zostera/django-jeaves/',
    license='MIT',
    install_requires=[
        'Django>=1.9',
    ]
)
