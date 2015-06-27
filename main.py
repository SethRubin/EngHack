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


# def query_words

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
