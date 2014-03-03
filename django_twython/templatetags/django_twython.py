'''
Created on 14/giu/2013

@author: Marco Pompili
'''

from twython import Twython
from django.conf import settings
from twython import exceptions 
from django import template

register = template.Library()

class TwitterTimelineNode(template.Node):
    
    def __init__(self, args):
        self.username = args[1]
        self.count = args[2]
        self.twitter = Twython(
                               settings.TWITTER_CONSUMER_KEY,
                               settings.TWITTER_CONSUMER_SECRET,
                               settings.TWITTER_ACCESS_TOKEN,
                               settings.TWITTER_ACCESS_TOKEN_SECRET
                               )
    
    def render(self, context):
        try:
            timeline = self.twitter.get_user_timeline(
                                                      screen_name=self.username,
                                                      count=self.count
                                                      )
        
            context['timeline'] = timeline
        
            return ''
        except exceptions.TwythonError as e:
            print("Django Twython Error: %s" %e)

@register.tag
def twitter_user_timeline(parser, token):
    """
        User Time-line tag.
        
        Usage::
            {% twitter_user_timeline <twitter-username> <number-of-twits> %}
    """
    return TwitterTimelineNode(token.split_contents())
    