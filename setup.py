from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()
setup(
    name='pencepay-python',
    version='0.0.1',
    packages=[
        'pencepay',
        'pencepay.settings',
        'pencepay.utils',
    ],
    url='https://github.com/opencbsoft/pencepay-python',
    license='MIT',
    author='Luci Furtun',
    author_email='lucianfurtun@gmail.com',
    description='A pencepay class to help with payments.',
    long_description=long_description,
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='pencepay payment class',
    install_requires=['requests', 'marshmallow==3.0.0a1'],
)
