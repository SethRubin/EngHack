import os, sys
import psycopg2
import urlparse
import json

from flask import Flask, request
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
    last_sent = db.Column(db.DateTime)
    pub_date = db.Column(db.DateTime)

    def __init__(self, email, word):
        self.email = email
        self.word = word
        self.pub_date = datetime.utcnow()

    def __repr__(self):
        return "Email: {0} , word: {1}".format(self.email, self.word)

    def __str__(self):
        return "Email: {0} , word: {1}".format(self.email, self.word)

# class Word(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     word = db.Column(db.String, unique=True)
#     last_updated = db.Column(db.DateTime)
#     # prev_averages = db.Column(SQLAlchemy.dialects.postgresql.ARRAY(db.Integer, dimensions=7))
#     pub_date = db.Column(db.DateTime)

#     def __init__(self, word):
#         self.word = word
#         # self.prev_averages = [None for i in xrange(7)]
#         self.pub_date = datetime.utcnow()

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
    #bulk_email('yo cron', ['h353wang@uwaterloo.ca', 'seth.h.rubin@gmail.com'])
    pass

@app.route("/create_all/")
def create_all():
    db.create_all()
    return "Created all!"

@app.route("/add_subscription/", methods=['POST'])
def add_subscription():
    email=request.form['email']
    word=request.form['word']
    newSub = Subscription(email, word)
    db.session.add(newSub)
    db.session.commit()
    return "Subscribed " + email + " to " + word

@app.route("/get_all_subscription/")
def get_all_subscription():
    subs = Subscription.query.all()
    subsStr = []
    for sub in subs:
        subsStr.append(str(sub))
    return json.dumps(subsStr)

@app.route("/remove_subscription/", methods=['POST'])
def remove_subscription():
    email=request.form['email']
    word=request.form['word']
    del_subscription = Subscription(email, word)
    db.session.add(del_subscription)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
