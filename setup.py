from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='table_bert',
    version='0.1',  # Required
    description='Learning contextual representations on textual and structured tabular data',
    author='Pengcheng Yin',
    author_email='pcyin@cs.cmu.edu',
    packages=find_packages(exclude=['exp_runs', 'scripts', 'preprocess', 'utils']),
    python_requires='>=3.6'
)
