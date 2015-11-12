from flask import Flask, render_template, request, session, redirect, url_for
import urllib2, json

NYTIMES_TOP_STORIES = "f8855388b9dccd77285db343bee18bd2:6:73424671"

app = Flask(__name__)

@app.route('/')
def index():
    request = urllib2.Request("http://api.nytimes.com/svc/topstories/v1/technology.json?api-key=" + NYTIMES_TOP_STORIES)
    response = urllib2.urlopen(request)
    page = json.load(response)
    return "<h1>" + str(page['results'][0]['title']) + "</h1><br><em>" + str(page['results'][0]['byline']) + "</em><br>" + str(page['results'][0]['abstract'])

if __name__=="__main__":
    app.debug = True
    app.secret_key = "p0NZLhPzCbjSJxxo"
    app.run(host='0.0.0.0', port=8080)
