# Configuration file for hms_twitter

# RabbitMQ

RABBIT_HOST = 'localhost'                   # Address of the server
RABBIT_EXCHANGE = 'haum'                    # Name of the direct exchanger

RABBIT_ROUTING_KEYS = ['twitter.*']       # List of routing keys to listen to

# Twitter

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# Import production settings if existing

try:
    from hms_twitter.settings_prod import *
except ImportError:
    pass
