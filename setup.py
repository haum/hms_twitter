from distutils.core import setup

from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()



setup(
    name='hms_twitter',
    version='1.0',
    packages=['hms_twitter'],
    scripts=['bin/hms_twitter'],

    url='https://github.com/haum/hms_twitter',
    license='MIT',

    author='Sébastien Vallée (seb_vallee)',
    author_email='sebastien@svallee.fr',

    description='HAUM\'s twitter microservice',
    long_description=long_description,

    classifiers = [
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    install_requires=['twitter', 'pika', 'hms_base>=2.0,<3', 'irc', 'coloredlogs']
)
