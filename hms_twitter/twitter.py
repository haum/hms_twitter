import logging

from twitter import *
from hms_twitter import settings

def get_logger():
    return logging.getLogger(__name__)

class HmsTwitter:
    def __init__(self):

        print('init')

        self.api = Twitter(auth=OAuth(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET, settings.CONSUMER_KEY, settings.CONSUMER_SECRET), retry=True)

    def tweet(self, status):
        try:
            tweet = api.statuses.update(status=status)
            id = tweet['id']
            return id
        except Exception as e:
            get_logger().info(e)
            # for error in e.response_data['errors']:
            #     err_message = error['message']
            return 0


    # def answer(self, status, id):
    #     print('Answering to ', id, ' with : ', status, ' !')
    #     self.api.update_status(status, id)
    #
    # def retweet(self, id):
    #     print('ReTweeting ', id, ' !')
    #     self.api.retweet(id)
    #
    # def delete(self, id):
    #     print('Deleting ', id, ' !')
    #     self.api.destroy_status(id)
