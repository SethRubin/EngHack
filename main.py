from flask import Flask, render_template
import json
import time

from bulk_email import bulk_email
from database_model import get_words, get_all_emails, Subscription
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

@app.route("/get_trending_data/<word>")
def get_trending_data(word):
    return word_trending_data(word)

# def query_words
def filter_by_trending(words):
    trending_words = []
    i = 0
    while i < len(words):
        try:
            if is_word_trending(words[i]):
                words.append(words[i])
            i += 1
        except:
            time.sleep(60*15)

    return trending_words

send_email = BackgroundScheduler(daemon=True)
@send_email.scheduled_job('interval', minutes=1)
def timed_update():
    emails = get_all_emails()
    for email in emails:
        subsribed_words = get_words(email)
        words_to_send = filter_by_trending(subsribed_words)
        bulk_email(words_to_send, [user])

send_email.start()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
