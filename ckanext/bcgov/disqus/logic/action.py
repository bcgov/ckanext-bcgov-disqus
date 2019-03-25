def post_disqus_comment(context, comment_dict):
    '''
    Uses Disqus api to post a guest comment.
    Comment_dict :
        thread :
        message :
        author_email :
        author_name :
    '''

    import urllib2
    import urllib
    import json

    import pycurl

    from disqusapi import DisqusAPI
    import cStringIO

    public_api = 'qUpq4pP5Kg6bKmAraTSig2lwghWO5KNqCTmiCdRHD66rgGTWKVCQloJVqvpfe5HI'
    secret_api = 'r7fjQCL36LDS2fTWMjLHYZpsiN99MnXZ5D6n8byIMPPZ1x9ohMvnTDOpczHba9N9'

    '''
        Add the secret api to comment dictionary.
        The secret api is taken from the Disqus account(Login to your Disqus account to get the secret api key).
    '''
    comment_dict['api_secret'] = secret_api
    comment_dict['forum'] = u'h3testblog'
    identifier = comment_dict['thread']
    comment_dict['thread'] = 'ident:' + identifier
    # Set the fields string :
    fields_string = ''
    url = 'http://disqus.com/api/3.0/posts/create.json'

    #    url= 'https://disqus.com/api/3.0/threads/list.json?api_secret=frFrznmdh6WlR5Xz9dvv6749Ong8l4hWprLdFItoa743d9SwGJ7koQLJuyhKZ7A0&forum=h3testblog'

    #     comment_dict = {'api_secret' : secret_api,
    #                     'forum': 'h3testblog'}
    #     data_string = urllib.quote(json.dumps(comment_dict))
    #
    #     try:
    #         request = urllib2.Request('https://disqus.com/api/3.0/threads/list.json')
    #         request.add_header('Accept', 'application/json')
    #         request.add_header('Authorization', public_api)
    # #        request.add_header('Authorization', secret_api)
    #         response = urllib2.urlopen(request, data_string)
    # #        assert response.code == 200
    #
    #         response_dict = json.loads(response.read())
    # #        assert response_dict['success'] is True
    # #        result = response_dict['result']
    #     except Exception:
    #         pass

    # Get the thread id first :
    thread_dict = {'api_secret': secret_api,
                   'forum': 'h3testblog',
                   'thread': 'ident:' + identifier}

    thread_string = ''
    # Construct the post fields string
    for key, value in thread_dict.iteritems():
        thread_string += key + '=' + value + '&'
    thread_string = thread_string[:-1]

    buf = cStringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(
        pycurl.URL, 'https://disqus.com/api/3.0/threads/set.json?' + thread_string)
    c.setopt(pycurl.VERBOSE, 0)
    c.setopt(c.WRITEFUNCTION, buf.write)

    c.perform()

    response = json.loads(buf.getvalue()).get('response', [])

    thread = None
    if len(response) > 0:
        thread = response[0]

    if thread:
        thread_id = thread.get('id', None)

    buf.close()

    comment_dict['thread'] = thread_id
    del comment_dict['forum']

    #     from disqusapi import DisqusAPI
    #
    #     client = DisqusAPI(secret_api, public_api)
    #     client.posts.create(api_secret=public_api, **comment_dict)
    #
    # Construct the post fields string
    fields_string = ''
    for key, value in comment_dict.iteritems():
        fields_string += key + '=' + value + '&'
    fields_string = fields_string[:-1]

    buf = cStringIO.StringIO()

    # Post the comment using curl
    c = pycurl.Curl()
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.VERBOSE, 0)
    c.setopt(c.POSTFIELDS, fields_string)
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.perform()

    buf.close()