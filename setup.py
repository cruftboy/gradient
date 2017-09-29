from setuptools import setup


setup(
   name='gradient',
   version='1.0',
   description='module makes gradients',
   author='Jasper Wood',
   author_email='jasperwoodlaptop@gmail.com',
   url = 'https://github.com/cruftboy/gradient',
   download_url = 'https://github.com/cruftboy/gradient.git',
   packages=['gradient'],  #same as name
   install_requires=['webcolors'], #external packages as dependencies
)