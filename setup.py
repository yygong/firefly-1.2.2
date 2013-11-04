from setuptools import setup, find_packages
import sys, os

version = '1.2.2'

setup(name='firefly',
      version=version,
      description="game server framework",
      long_description="""\
game server framework""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='twisted pb memcached',
      author='Lan Jinmin',
      author_email='zhuiming.mu@gmail.com',
      url='9miao.com',
      license='firefly',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	  scripts = ['firefly/script/firefly-admin.py'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
		  "twisted",
		  "zope.interface",
		  
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
