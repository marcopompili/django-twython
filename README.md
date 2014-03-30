django-twython
==============
Twitter integration for django using the excellent Twython wrapper. This application implements some tags and templates that allows to display twits based on an user in a web page.

Requirements
------------
- [Django => 1.6](http://www.djangoproject.org)
- [Twython](https://github.com/ryanmcgrath/twython)

Installation
------------
This application can be installed using pip. First clone this repository then install the application locally like this:
```
pip -e install django-twython
```

Configuration
-------------
Set the app in the INSALLED_APPS settings.py variable.

```python
INSTALLED_APPS = (
	[...]
	'twython',
	'django_twython'
	[...]
)
```

And then set some parameters in the settings.py:

```python
TWITTER_CONSUMER_KEY = '...'
TWITTER_CONSUMER_SECRET = '...'
TWITTER_ACCESS_TOKEN = '...'
TWITTER_ACCESS_TOKEN_SECRET = '...'
```

Examples
--------
First include the tag library:
```
{% load django_twython %}
```

Then call the tag in a template, like this:
```
{% twitter_user_timeline_data <username> <number-of-post-to-show> %}
	{% for twit in timeline %}
		<div class="twit">
			<p>
				{{twit.text|safe}}
			</p>
		</div>
	{% endfor %}
```

Or just use the include tag version, for example:
```
{% twitter_user_timeline "<username>" count="4" %}
```
