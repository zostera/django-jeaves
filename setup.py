import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

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
