import os, sys
import psycopg2
import urlparse
import json

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from bulk_email import bulk_email
from apscheduler.schedulers.background import BackgroundScheduler

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=False)
    word = db.Column(db.String, unique=False)
    pub_date = db.Column(db.DateTime)

    def __init__(self, email, word):
        self.email = email
        self.word = word
        self.pub_date = datetime.utcnow()

    def __repr__(self):
        return "Email: {0} , word: {1}".format(self.email, self.word)

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

@app.route("/createall")
def createAll():
    db.create_all()
    return "Created all!"

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

@app.route("/getallsub")
def getAllSub():
    try:
        subs = []#Subscription.query.all()
        return subs
        #return json.dumps(subs)
    except:
        return "Error occurred:", sys.exc_info()[0]

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
