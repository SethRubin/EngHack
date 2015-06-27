import os, sys
import psycopg2
import urlparse
import json

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__, template_folder='template')
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


def get_all_emails():
    subs = Subscription.query.all()
    s = set([sub.email for sub in subs])
    return list(s)

def get_words(email):
    subs = Subscription.query.filter_by(email=email)
    s = set([sub.word for sub in subs])
    return list(s)

# @app.route("/remove_subscription/", methods=['POST'])
# def remove_subscription():
#     email = str(request.form['email'])
#     word = str(request.form['word'])
#     del_subscription = Subscription(email, word)
#     db.session.delete(del_subscription)
#     db.session.commit()
#     return "Removed"
