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

4.  Add edcdisqus.api_key, edcdisqus.forum_name, edcdisqus.access_token, edcdisqus.api_secret and edcdisqus.widget_api_key to the 
    ckan.ini file using the values you get from disqus
    
    
Usage
============
This follows the same scheme as other CKAN plugins and requires you to add it to pages using: 
```
h.comments_block()
```

Additionally you can (and should) override the disclaimer by extending templates/package/comments_block.html



    Original Repo Copyright 2018, Province of British Columbia.
