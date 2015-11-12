import urllib2, json

# API Keys
NYTIMES_TOP_STORIES = "f8855388b9dccd77285db343bee18bd2:6:73424671"

def top_stories(section='home'):
    data = json.load(
        urllib2.urlopen(
            urllib2.Request(
                "http://api.nytimes.com/svc/topstories/v1/{0}.json?api-key={1}".format(
                    section, NYTIMES_TOP_STORIES
                ))))['results']
    return data

def format_article(article):
    return u"<h1><a href=\"{url}\">{title}</a></h1><em>{date}</em><h3>{byline}</h3><p>{abstract}</p><br>".format(
        url=article['url'],
        title=article['title'],
        date=article['published_date'],
        byline=article['byline'],
        abstract=article['abstract']
    )