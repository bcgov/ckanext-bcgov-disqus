# Copyright  2015, Province of British Columbia 
# License: https://github.com/bcgov/ckanext-bcgov/blob/master/license 
 
from setuptools import setup, find_packages
import sys, os

# for version variable
exec(open("ckanext/bcgov/disqus/version.py").read())

setup(
    name='ckanext-bcgov-disqus',
    version=version,
    description="CKAN Extension - BCGov Disqus.",
    long_description="""\
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Brandon Sharratt',
    author_email='brandon@highwaythreesolutions.com',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.bcgov', 'ckanext.bcgov.disqus'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pycurl==7.43.0.1',
        'validate_email==1.2',
    ],
    entry_points=\
    """
    [ckan.plugins]
    # Add plugins here, eg
    edc_disqus = ckanext.bcgov.disqus.plugin:EDCDisqusPlugin
    """,
)
