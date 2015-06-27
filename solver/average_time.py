import json
from dateutil import parser
from datetime import date, timedelta
from twitter_scrapper import get_twitter_data

def get_average_time(searches):
    if (len(searches) < 100):
        return None
    newest = parser.parse(searches[0]['created_at'])
    oldest = parser.parse(searches[-1]['created_at'])

    return (newest - oldest).total_seconds()/100

def get_past_average_times(word):
    average_times = [] # first element is avg time now. Every other element is past avg times
    offset = -1
    for i in range(0, 7):
        end_date = date.today() + timedelta(days=offset)
    	until = end_date.strftime("%Y-%m-%d")
    	searches = get_twitter_data(word, until)
        average_times.append(get_average_time(searches))
        offset = offset - 1
    return average_times