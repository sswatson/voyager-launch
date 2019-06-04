
from setuptools import setup

setup(name='voyager-launch',
      version='0.1',
      description='Open DataFrames in Voyager',
      url='http://github.com/sswatson/voyager',
      author='Samuel S. Watson',
      author_email='samuel.s.watson@gmail.com',
      license='MIT',
      packages=['voyager'],
      install_requires = [
            'pandas',
      ],
      include_package_data=True,
      zip_safe=False)