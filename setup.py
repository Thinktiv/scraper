from setuptools import setup, find_packages

VERSION = (0, 2, 2)
__version__ = '.'.join(map(str, VERSION))

setup(
    name='scraper',
    version=__version__,
    description='Scraping Tool',
    long_description=open('README.rst').read(),
    author='Sandip Agarwal',
    author_email='sandip.agarwal@joshlabs.in',
    url='http://github.com/Thinktiv/scraper',
    download_url='http://github.com/Thinktiv/scraper/downloads',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        "simplejson==2.6.1",
        "PIL==1.1.7",
        "BeautifulSoup==3.2.1",
        "eventlet==0.14.0"
    ],
)
