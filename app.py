from flask import Flask, render_template, request, session, redirect, url_for
from apis import dictionary, nytimes
import urllib2, json

app = Flask(__name__)
app.jinja_env.line_statement_prefix = '%'

@app.route('/')
def index():
    return render_template("home.html");

@app.route('/debug/', methods=["GET"])
def backfrip_debug():
    search = request.args.get('search')
    defs = dictionary.query(search)
    return render_template("debug.html", search=search, defs=defs)

if __name__=="__main__":
    app.debug = True
    app.secret_key = "p0NZLhPzCbjSJxxo"
    app.run(host='0.0.0.0', port=8080)
