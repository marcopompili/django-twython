django-twython
==============

Twitter integration for django using the Twython wrapper.


Requirements
------------
- [twython](https://github.com/ryanmcgrath/twython)


Installation
------------
Set the app in the INSALLED_APPS settings.py variable.

```python
INSTALLED_APPS = '... twython ...'

```

And then set some parameters in the settings.py.

```python
TWITTER_CONSUMER_KEY = '...'
TWITTER_CONSUMER_SECRET = '...'
TWITTER_ACCESS_TOKEN = '...'
TWITTER_ACCESS_TOKEN_SECRET = '...'

```
