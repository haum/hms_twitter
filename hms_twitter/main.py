import logging
from threading import Thread

import coloredlogs

from hms_base.client import Client
from hms_base.decorators import topic

from hms_twitter import settings
from hms_twitter.twitter import HmsTwitter

COMMANDS = ['tweet', 'rt', 'delete', 'reply']

def get_logger():
    return logging.getLogger(__name__)

def main():
    """Entry point of the program."""

    # Logging
    coloredlogs.install(level='INFO')

    # Connect to Rabbit
    rabbit = Client('hms_twitter', settings.RABBIT_EXCHANGE,
                    settings.RABBIT_ROUTING_KEYS)

    rabbit.connect(settings.RABBIT_HOST)
    twitter = HmsTwitter()

    # Closure, cannot use @topic directly on method
    @topic('twitter.query')
    def query_closure(client, topic, dct):
        command = dct['command']

        if command.startswith('tweet'):
            status = dct['status']
            twitter.tweet(status)
        elif command.startswith('reply'):
            status = dct['status']
            id = dct['id']
            twitter.reply(status, id)
        elif command.startswith('rt'):
            id = dct['id']
            twitter.rt(id)
        elif command.startswith('delete'):
            id = dct['id']
            twitter.delete(id)

    rabbit.listeners.append(query_closure)

    get_logger().info("Starting passive consumming...")
    rabbit.start_consuming()
