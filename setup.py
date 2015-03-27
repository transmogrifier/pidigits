# -*- coding: utf-8 -*-
#   Copyright 2015 Sameer Suhas Marathe
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""Setup file for Pidigits"""

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pidigits',
      version='0.1',
      description=('Generate arbitrary number of digits of'
                   ' Pi using a streaming algorithm.'),
      long_description=readme(),
      url='https://github.com/transmogrifier/pidigits',
      author='Sameer Marathe',
      author_email='transmogrifier@gmail.com',
      license='Apache License 2.0',
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: End Users/Desktop'
      ],
      keywords='mathematics number_theory pi spigot_algorithm',
      packages=['pidigits'],
      install_requires=[],
      test_suite='pidigits._tests',
      zip_safe=False)

