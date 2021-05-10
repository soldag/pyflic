from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_description = f.read()


setup(name='pyflic',
      version='0.4.0',
      description='Python library to connect to and interact with Flic buttons.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='soldag',
      author_email='soeren_oldag@freenet.de',
      url='https://github.com/soldag/pyflic',
      license='CC0 1.0 Universal',
      packages=find_packages(),
     )
