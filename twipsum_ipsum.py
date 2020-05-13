import tweepy
import json
import datetime
from tweepy import OAuthHandler

import generators as gens
import text_formatters as forms

class TweetMiner:
    result_limit = 20
    data = []
    api = False

    twitter_keys = {
        'consumer_key' : '',
        'consumer_secret' : '',
        'access_token' : '',
        'access_secret' : ''
    }

    def __init__(self, keys_dict = twitter_keys, api = api, result_limit = 20):

        self.twitter_keys = keys_dict

        auth = OAuthHandler(keys_dict['consumer_key'], keys_dict['consumer_secret'])
        auth.set_access_token(keys_dict['access_token'], keys_dict['access_secret'])

        self.api = tweepy.API(auth)
        self.twitter_keys = keys_dict

        self.result_limit = result_limit

    def mine_user_tweets(self, user = 'TheAtlantic', mine_retweets = False, max_pages = 5):
    # Chage user in order to mine a different account
        data = []
        last_tweet_id = False
        page = 1

        while page <= max_pages:
            if last_tweet_id:
                statuses = self.api.user_timeline(screen_name = user,
                                                  count = self.result_limit, # result_limit defined before __init__
                                                  max_id = last_tweet_id - 1,
                                                  tweet_mode = 'extended',
                                                  include_retweets = True
                                                 )
            else:
                statuses = self.api.user_timeline(screen_name = user,
                                                  count = self.result_limit,
                                                  tweet_mode = 'extended',
                                                  include_retweets = True
                                                 )
            for item in statuses:
                mined = {
                # For this project, I only need text data. Keep everything incase if needed later.
                    # 'tweet_id' : item.id,
                    # 'name' : item.user.name,
                    # 'screen_name' : item.user.screen_name,
                    # 'retweet_count' : item.retweet_count,
                    'text' : item.full_text,
                    # 'mined_at' : datetime.datetime.now(),
                    # 'created_at' : item.created_at,
                    # 'favorite_count': item.favorite_count,
                    # 'hashtags' : item.entities['hashtags'],
                    # 'statuses_count' : item.user.statuses_count,
                    # 'location' : item.place,
                    # 'source_device' : item.source
                }

                # try:
                #     mined['retweet_text'] = item.retweeted_status.full_text
                # except:
                #     mined['retweet_text'] = 'None'
                #
                # try:
                #     mined['quote_text'] = item.quoted_status.full_text
                #     mined['quote_screen_name'] = status.quoted_status.user.screen_name
                # except:
                #     mined['quote_text'] = 'None'
                #     mined['quote_screen_name'] = 'None'

                last_tweet_id = item.id
                data.append(mined)

            page += 1

        return data

miner = TweetMiner()

username = input("Please enter a Twitter username: ")
tweet_list = miner.mine_user_tweets(user = username)

sentences_to_generate = input("Please enter how many sentences you would like: ")
sentence_lengths = gens.num_of_sentences(int(sentences_to_generate))

formatted_tweets = forms.format_text(tweet_list)
tweet_words = forms.create_words_list(formatted_tweets)
words_no_links = forms.remove_links(tweet_words)
sentence_lists = forms.word_selection(sentence_lengths, words_no_links)
paragraph = forms.make_sentences(sentence_lists)

print (paragraph)

# https://towardsdatascience.com/tweepy-for-beginners-24baf21f2c25
