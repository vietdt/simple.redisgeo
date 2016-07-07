from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='simple.redisgeo',
      version=version,
      description="Test redis geo commands implementation",
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='redis geo geohash radius python',
      author='Viet Dinh',
      author_email='vietdt@gmail.com',
      url='https://github.com/vietdt/simple.redisgeo',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['simple'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'redis',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      test_suite='nose.collector',
      tests_require=['nose'],
      )
