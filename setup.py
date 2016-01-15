from setuptools import setup
from subprocess import check_output
from sys import platform

deps = ['requests', 'sleekxmpp']

if platform == 'win32':
    deps.append('pypiwin32')

version_parts = (check_output(['git', 'describe', '--dirty=+dirty'])
                 .decode()
                 .rstrip('\n')
                 .lstrip('v')
                 .split('-'))
if len(version_parts) == 1:
    version, = version_parts
else:
    version_parts[-1] = version_parts[-1].replace('+', '.')
    version = '{}.dev{}+{}'.format(*version_parts[:3])

setup(
    name='ntfy',

    version=version,

    description='A utility for sending push notifications',

    url='https://github.com/dschep/ntfy',

    author='Daniel Schep',
    author_email='dschep@gmail.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        'Environment :: Console',

        'Intended Audience :: End Users/Desktop',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='push notification',

    packages=['ntfy', 'ntfy.backends'],
    package_data={'ntfy': ['icon.png', 'icon.ico']},

    install_requires=deps,

    entry_points={
        'console_scripts': [
            'ntfy = ntfy.cli:main',
        ],
    },
)
