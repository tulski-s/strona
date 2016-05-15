# flask
from flask import Flask, redirect, render_template

# config
app = Flask(__name__)
app.config.from_object(__name__)


# views
@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/CV')
def CV():
    return render_template('CV.html', title="CV")

# posts
@app.route('/proxy_harvester')
def post_proxy_harvester():
    return render_template('proxy_harvester.html')

@app.route('/creepy_scraper')
def post_creepy_scraper():
    return render_template('creepy_scraper.html')