from flask import Flask, render_template, request, session, redirect, url_for
from apis import dictionary, nytimes, tumblr
import urllib2, json, os.path

app = Flask(__name__)
app.jinja_env.line_statement_prefix = '%'

@app.route('/', methods=["GET"])
def index():
    search = request.args.get('search')
    defs = dictionary.query(search)
    posts = tumblr.tagged_posts(search)
    articles = nytimes.article_search(search)
    return render_template(
        "home.html",
        search=search,
        defs=defs,
        posts=posts,
        articles=articles
    )
    
@app.route('/about/')
def about():
    return render_template("about.html");

@app.route('/debug/', methods=["GET"])
def backfrip_debug():
    search = request.args.get('search')
    defs = dictionary.query(search)
    posts = tumblr.tagged_posts(search)
    articles = nytimes.article_search(search)
    return render_template(
        "debug.html",
        search=search,
        defs=defs,
        posts=posts
    )

if __name__=="__main__":
    app.debug = True
    app.secret_key = "p0NZLhPzCbjSJxxo"
    app.run(host='0.0.0.0',
        port=(8080 if os.path.isfile('cloudy') else 8000)
        # (Account for the fact that Cloud9 doesn't do port 8000
        #  with an arbitrary file check. Don't worry, Git ignores it.)
    )
