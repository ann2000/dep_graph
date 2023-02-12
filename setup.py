from setuptools import setup, find_packages

setup(
    name='dep_graph',
    version='0.1',
    packages=find_packages(),
    author='Ann Rose Cherian',
    author_email='roseanncherian@gmail.com',
    description='This package can be used to read a JSON file from a fixed filesystem location containing a list of packages and their dependencies, and reconstructs the full dependency graph.',
    install_requires=[
        'networkx',
        'matplotlib'
    ],
)