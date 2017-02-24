from setuptools import setup, find_packages

setup(name='pyxmlconc',
      version='0.2',
      description='A very simple concordancer with XML support.',
      url='https://github.com/IngoKl/PyXMLConc',
      author='Ingo Kleiber',
      author_email='ingo@kleiber.me',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False)
