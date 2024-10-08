from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_description = f.read()


setup(name='pyflic',
      version='2.0.4',
      description='Python library to connect to and interact with Flic buttons.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='soldag',
      author_email='soeren_oldag@freenet.de',
      url='https://github.com/soldag/pyflic',
      license='MIT',
      packages=find_packages())
