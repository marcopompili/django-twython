"""
Created on 14/giu/2013

@author: Marco Pompili
"""

import datetime

from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django import template

from twython import Twython
from twython import exceptions

register = template.Library()


def twython_get_api():
    return Twython(
        settings.TWITTER_CONSUMER_KEY,
        settings.TWITTER_CONSUMER_SECRET,
        settings.TWITTER_ACCESS_TOKEN,
        settings.TWITTER_ACCESS_TOKEN_SECRET
    )


class TwitterTimelineNode(template.Node):
    def __init__(self, args):
        self.username = args[1]
        self.count = args[2]

        self.twitter = twython_get_api()

    def render(self, context):
        try:
            timeline = self.twitter.get_user_timeline(
                screen_name=self.username,
                count=self.count
            )

            context['timeline'] = timeline

            return ''
        except exceptions.TwythonError as e:
            print("Django Twython Error: %s" % e)


@register.tag
def twitter_user_timeline_data(parser, token):
    """
        User Time-line tag.
        
        Usage::
            {% twitter_user_timeline <twitter-username> <number-of-twits> %}
    """
    return TwitterTimelineNode(token.split_contents())


@register.inclusion_tag('django_twython/timeline.html')
def twitter_user_timeline(user, *args, **kwargs):
    try:
        api = twython_get_api()

        timeline = api.get_user_timeline(
            screen_name=user,
            count=kwargs.get('count', '5')
        )

        return {
            'timeline': timeline
        }

    except exceptions.TwythonError as e:
        print("Django Twython Error: %s" % e)


@register.filter(name='html_for_tweet')
def twython_html_for_twit(value):
    """
        Transforms the text of the twit into an html version.

        Usage::
            {{ twit|html_for_tweet }}
    :param value: The twit
    :return:
    """
    return mark_safe(Twython.html_for_tweet(value))


@register.filter(name='twitter_date_format')
def twitter_date_format(value):
    """

    :param value:
    :return:
    """
    created_ad = datetime.datetime.strptime(value, "%a %b %d %H:%M:%S +0000 %Y")
    now = datetime.datetime.now()

    return (now - created_ad).days