from flask import Flask
import json

from bulk_email import bulk_email
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

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

@sendEmail.scheduled_job('interval', seconds=10)
def timed_job():
    bulk_email('yo cron', ['h353wang@uwaterloo.ca', 'seth.h.rubin@gmail.com'])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
