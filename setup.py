from setuptools import setup, find_packages
import os

version = '3.2.1'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'jquery', 'test_jquery.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.jquery',
    version=version,
    description="fanstatic jQuery.",
    long_description=long_description,
    classifiers=[
        'Development Status :: 6 - Mature',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    keywords='fanstatic jQuery WSGI middleware static asset',
    author='Fanstatic Developers',
    author_email='fanstatic@googlegroups.com',
    url='https://bitbucket.org/fanstatic/js.jquery',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
    ],
    entry_points={
        'fanstatic.libraries': [
            'jquery = js.jquery:library',
        ],
    },
)
