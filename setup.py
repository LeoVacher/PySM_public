from setuptools import setup

setup(name='pysm',
      version='2.0',
      description='Code for simulating the Galactic microwave sky.',
      url='http://github.com/bthorne93/PySM_Public',
      author='Ben Thorne',
      author_email='ben.thorne@physics.ox.ac.uk',
      license='MIT',
      packages=['pysm'],
      package_dir={'pysm': 'pysm'},
      install_requires=['healpy', 'numpy', 'scipy', 'astropy'],
      zip_safe=False)

