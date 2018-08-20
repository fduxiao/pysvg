from io import open
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="pysvg",
    version='0.0.1',
    description='A python tool to make svg images',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/fduxiao/pysvg",
    author="fduxiao",
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
    ],
    keywords='svg make',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
    install_requires=[''],
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/fduxiao/pysvg/issues',
        # 'Funding': 'https://github.com/fduxiao/pysvg/issues',
        # 'Say Thanks!': 'https://github.com/fduxiao/pysvg/issues',
        'Source': 'https://github.com/fduxiao/pysvg/',
    },
)
