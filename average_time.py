import json
from dateutil import parser

# data = json.loads(open('test-json').read())


def get_average_time(searches):
	for search in searches:
        newest = parser.parse(data['statuses'][0]['created_at'])
        oldest = parser.parse(data['statuses'][-1]['created_at'])

# print (newest - oldest).total_seconds()/100