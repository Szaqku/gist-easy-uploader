from setuptools import setup

setup(name='gist-easy-uploader',
      version='1.0',
      description='Gist easy uploader',
      url='http://github.com/Szaqku/gist-easy-uploader',
      author='Szaqku',
      author_email='szaqku@gmail.com',
      license='MIT',
      packages=['src'],
      install_requires=[
          'clipboard', 'requests'
      ],
      zip_safe=False)