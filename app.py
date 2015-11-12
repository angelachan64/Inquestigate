from flask import Flask, render_template, request, session, redirect, url_for
from apis import nytimes
import urllib2, json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html");

@app.route('/debug/')
def backfrip_debug():
    data = nytimes.top_stories('technology')
    output = "<head><style>div{background-color:#cccccc;padding:1em;margin:\
1em;font-family:sans-serif;width:40%;display:inline-block;vertical-align:top;\
}</style></head><body>"
    for article in range(len(data)):
        output += u"<div id=\"{0}\"><h2 style=\"float:right;color:#808080\">\
<i>{0}</i></h2>{1}</div>".format(
            article, nytimes.format_article(data[article]))
    return output + "</body>"

if __name__=="__main__":
    app.debug = True
    app.secret_key = "p0NZLhPzCbjSJxxo"
    app.run(host='0.0.0.0', port=8000)
