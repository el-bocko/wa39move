from distutils.core import setup
from setuptools import find_packages
setup(name='wa39move',
 version='0.1',
 author='DSSS',
 author_email='steffen.bockrath@fau.de',
 packages=find_packages(),
 install_requires=['numpy', 'Pillow', 'ipywidgets'])
