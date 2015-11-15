import urllib2, urllib, json

API_KEY = "SEGyqmqNhVfBEj2FqtjAUCPmopYJ65Me0Skr48bMClzyOSNwdt"

def tagged_posts(tag, before=None, limit=None, filter=None):
    if not tag:
        return
    data = json.load(
        urllib2.urlopen(
            urllib2.Request(
                "https://api.tumblr.com/v2/tagged?tag={}\
&before={}&limit={}&filter={}&api_key={}".format(
                    urllib.quote(tag.encode('utf8')), before, limit, filter, API_KEY)
                )))
    return data
