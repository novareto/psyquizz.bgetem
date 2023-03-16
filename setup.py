# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


version = '1.0.dev0'

tests_require = []

setup(name='psyquizz.bgetem',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='GPL',
      namespace_packages=['psyquizz'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'fanstatic',
          'js.jquery',
          'megrok.pagetemplate',
          'setuptools',
          'cromlech.file',
          'dolmen.widget.file',
          'xlrd'
      ],
      extras_require = {'test': tests_require},
      entry_points={
         'fanstatic.libraries': [
            'psyquizz.bgetem = psyquizz.bgetem:library',
         ],
      }
)
