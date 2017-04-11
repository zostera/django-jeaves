import os
import sys

from setuptools import setup

DIR = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(DIR, 'README.rst')).read()

cmd = sys.argv[-1]

if cmd == 'test':
    print("Running tests only on current environment.")
    print("Use `tox` for testing multiple environments.")
    os.system('django-admin.py test')
    sys.exit()

setup(
    name='django-jeaves',
    version='0.1',
    packages=['jeaves'],
    description='Django EAV using JSONField',
    long_description=README,
    author='Dylan Verheul',
    author_email='dylan@zostera.nl',
    url='https://github.com/zostera/django-jeaves/',
    license='MIT',
    install_requires=[
        'Django>=1.11',
    ]
)
