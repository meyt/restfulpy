import re
from os.path import join, dirname
from setuptools import setup, find_packages


# reading package version (without reloading it)
with open(join(dirname(__file__), 'restfulpy', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)


dependencies = [
    'nanohttp >= 0.19.2',
    'argcomplete',
    'ujson',
    'appdirs',
    'sqlalchemy',
    'alembic',
    'itsdangerous',
    'mako',
    'psycopg2',
    'redis',
    'pyyaml',
    'ua-parser',
    'user-agents',

    # Testing
    'requests',
    'webtest',
    'nose'
]


setup(
    name='restfulpy',
    version=package_version,
    description='A toolchain for developing REST APIs',
    author='Vahid Mardani',
    author_email='vahid.mardani@gmail.com',
    install_requires=dependencies,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'restfulpy = restfulpy:main'
        ]
    },
    test_suite='restfulpy.tests',
    license='MIT'
)
