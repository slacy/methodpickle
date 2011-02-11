import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

requires = []

setup(name='methodpickle',
      version='0.1.0',
      description='Simple method invocation pickling.',
      long_description=README,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        ],
      author='Steve Lacy',
      author_email='slacy@slacy.com',
      url='http://github.com/slacy/methodpickle',
      keywords=['python', 'method', 'pickle'],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="methodpickle",
      )
