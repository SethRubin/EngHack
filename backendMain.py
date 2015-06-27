import os
import psycopg2
import urlparse
import json

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from bulk_email import bulk_email
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=False)
    word = db.Column(db.String(80), unique=False)

    def __init__(self, email, word):
        self.email = email
        self.word = word

@app.route('/')
def hello_world():
    obj = {
        'key': 3,
        'key2': 5,
        'key3': 6 
    }
    return json.dumps(obj)

sendEmail = BackgroundScheduler(daemon=True)
sendEmail.start()

@sendEmail.scheduled_job('interval', seconds=100000)
def timed_job():
    bulk_email('yo cron', ['h353wang@uwaterloo.ca', 'seth.h.rubin@gmail.com'])

@app.route("/addsub")
def addSubscription():
    newSub = Subscription("allen.wang@hiswebsite.url", "girls")
    db.session.add(newSub)
    db.session.commit()
    return "Added girls for allen.wang@hiswebsite.url"

@app.route("/othersub")
def addOther():
    otherSub = Subscription("marko@marko.com", "potatoes")
    db.session.add(otherSub)
    db.session.commit()
    return "Added potatoes for marko@marko.com"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)