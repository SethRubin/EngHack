from twitter_credentials import twitter

def get_twitter_data(word, until):
    """
        params: word (string) - Represents the word to be searched.
    """
    twitter_search_data = twitter.search(q=word, 
                                        lang='en', 
										result_type='recent', 
										count="100",
										include_entities="false",
										until=until)

    searches = twitter_search_data['statuses']
    return searches