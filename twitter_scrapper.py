from twython import Twython


APP_KEY = 'j1N2l2HbIKBVCVUF8uX63G7By'
APP_SECRET = '7wzRUTJKCNZcb5S65lDIn0XEsjZQElCyElrMCnVVDv0OJqkCri'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

twitter_search_data = twitter.search(q='python', lang='en', result_type='recent', count=100) 
searches = twitter_search_data['statuses']
for search in searches:
	print search['text']
