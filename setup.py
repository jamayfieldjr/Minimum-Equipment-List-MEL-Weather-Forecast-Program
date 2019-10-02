from setuptools import setup


setup(name='melequiplist',
      version='1.2.0',
      description='MEL (Minimum Equipment List) Weather Forecast Program',
      url='http://github.com/jamayfieldjr/melequiplist',
      author='John Mayfield',
      author_email='jamayfieldjr@gmail.com',
      license='MIT',
      package_dir={'': 'lib'},
      packages=['melequiplist'],
      zip_safe=True,
      classifiers = [
                        "Development Status :: 5 - Production/Stable",
                        "License :: OSI Approved :: MIT License",
                        "Operating System :: OS Independent",
                        "Programming Language :: Python :: 2.6",
                        "Programming Language :: Python :: 2.7",
                        "Programming Language :: Python :: 3",
                        "Topic :: Scientific/Engineering"
                    ],
      keywords="aviation weather meteorology taf metar"
      

