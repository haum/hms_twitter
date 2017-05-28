from hms_twitter import settings
from twitter import *

t = Twitter(
    auth=OAuth(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET, settings.CONSUMER_KEY, settings.CONSUMER_SECRET), retry=True)
try:
    tweet = t.statuses.update(status='12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890')
    id = tweet['id']
except Exception as e:
    for error in e.response_data['errors']:
         err_message = error['message']
