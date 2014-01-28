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

Use it
------
First include the tag library:
```
{% load django_twython %}
```

Then call the tag in a template, like this for example:
```
{% twitter_user_timeline <username> <number-of-post-to-show> %}
	{% for twit in timeline %}
		<div class="twit">
			<p>
				{{twit.text|safe}}
			</p>
		</div>
	{% endfor %}
```