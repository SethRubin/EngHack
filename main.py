from flask import Flask
import json
import time

from bulk_email import bulk_email
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler


app = Flask(__name__)

@app.route('/')
def hello_world():
    obj = {
        'key': 3,
        'key2': 5,
        'key3': 6 
    }
    return json.dumps(obj)

send_email = BackgroundScheduler(daemon=True)
send_email.start()

@send_email.scheduled_job('interval', seconds=20)
def timed_update():
    
    # get information for the words
    # get the words to update
    # for people in databse, get their words, and send email

def query_words():
    while 
        try:
            WordStatus.write(word, is_word_trending(word))

        except:

            time.sleep(60*15)
    


# def query_words

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
