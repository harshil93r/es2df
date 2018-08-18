import os
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_version():
    basedir = os.path.dirname(__file__)
    with open(os.path.join(basedir, 'es2df/version.py')) as f:
        variables = {}
        exec(f.read(), variables)
        return variables.get('VERSION')
    raise RuntimeError('No version info found.')


setup(
    name='es2df',
    version=get_version(),
    url='https://github.com/harshil9968/es2df/',
    license='BSD',
    author='Harshil Rastogi',
    author_email='harshil9968@gmail.com',
    description='es2df is a small, minimalistic, Python library for '
           'translating elasticsearch results into pandas dataframe.',
    long_description=long_description,
    packages=['es2df'],
    zip_safe=True,
    platforms='any',
    install_requires=['pandas', 'elasticsearch'],
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        #'Development Status :: 2 - Pre-Alpha',
        #'Development Status :: 3 - Alpha',
        #'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        #'Development Status :: 6 - Mature',
        #'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',

    ]
)
