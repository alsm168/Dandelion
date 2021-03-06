import os
import re
from setuptools import find_packages
from setuptools import setup
import io, shutil
from distutils.extension import Extension

cmdclass = {}
ext_modules = []

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'dandelion', '__init__.py'), 'r') as f:
    init_py = f.read()
version = re.search('__version__ = "(.*)"', init_py).groups()[0]

with io.open(os.path.join(here, 'README.md'), 'r', encoding='utf-8') as f:
    README = f.read()
with io.open(os.path.join(here, 'CHANGES.md'), 'r', encoding='utf-8') as f:
    CHANGES = f.read()

install_requires = [
    'numpy',
    'Theano',
    ]

tests_require = [
    'mock',
    'pytest',
    'pytest-cov',
    ]
setup(
    name="Dandelion",
    version=version,
    description="A low-level deep learning framework",
    long_description="\n\n".join([README, CHANGES]),
    classifiers=[
        "Intended Audience :: Deep learning scientists and researchers",
        "License :: Mozilla Public License v2.0",
        "Programming Language :: Python :: 3.5",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        ],
    keywords="DL framework, Theano",
    author="David Leon (Dawei Leng)",
    author_email="daweileng@outlook.com",
    license="Mozilla Public License v2.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'testing': tests_require,
        },
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    )
