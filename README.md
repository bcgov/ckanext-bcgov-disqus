[![Join us on Slack](https://cldup.com/jWUT4QFLnq.png)](https://devopspathfinder.slack.com/messages/C915T1NEP)

ckanext-bcgov-disqus
=============

This extension provides disqus features on the [BC Data Catalogue](http://catalogue.data.gov.bc.ca).

Installation
============

1.  Activate virtual environment, e.g.

        $ . /usr/lib/ckan/default/bin/activate

2.  Install the extension. Switch to `ckanext-bcgov-disqus` extension directory and run the following command:

        python setup.py develop


3.  Update config file and add the following plugins to `ckan.plugins` list : `edc_disqus`.

4.  Update (or create) `import.ini` file inside `ckanext-bcgov/ckanext/bcgov/scripts/config`. Add `api_key`, `site_url` options (they should be the same as in your CKAN `.ini` file).


    Original Repo Copyright 2018, Province of British Columbia.
