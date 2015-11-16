import urllib2, urllib, json

# API Keys
NYTIMES_TOP_STORIES = "f8855388b9dccd77285db343bee18bd2:6:73424671"
NYTIMES_ARTICLE_SEARCH = "1252c739bd84d05b3c1c6a78c2f32d6b:15:73475840"

def top_stories(section='home'):
    data = json.load(
        urllib2.urlopen(
            urllib2.Request(
                "http://api.nytimes.com/svc/topstories/v1/{}.json?api-key={}".format(
                    section, NYTIMES_TOP_STORIES
                ))))['results']
    return data

def article_search(term): #section='home'
    if not term:
        return
    url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q="
    url += term
    url += '&api-key='
    url += NYTIMES_ARTICLE_SEARCH
    data = json.loads(urllib2.urlopen(url).read())['response']
    return data

def format_article(article):
    return u"<h1><a href=\"{url}\">{title}</a></h1><em>{day}, {date}</em><p>{body}</p><br>".format(
        url=article['web_url'],
        title=article['headline'],
        day=article['day_of_week'],
        date=article['pub_date'],
        body=article['body']
    )