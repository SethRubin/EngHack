from twython import Twython

APP_KEY = 'j1N2l2HbIKBVCVUF8uX63G7By'
APP_SECRET = '7wzRUTJKCNZcb5S65lDIn0XEsjZQElCyElrMCnVVDv0OJqkCri'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)