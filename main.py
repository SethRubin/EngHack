from flask import Flask, render_template
import json
import time

from bulk_email import bulk_email
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler


app = Flask(__name__, template_folder='template')

@app.route('/')
def hello_world():
    template_vars = {}
    return render_template('index.html', **template_vars)

@app.route("/create_all/")
def create_all():
    db.create_all()
    return "Created all!"

@app.route("/add_subscription/", methods=['POST'])
def add_subscription():
    email = str(request.form['email'])
    word = str(request.form['word'])
    newSub = Subscription(email, word)
    db.session.add(newSub)
    db.session.commit()
    return "Subscribed " + email + " to " + word

# def query_words

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
