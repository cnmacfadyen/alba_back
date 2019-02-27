import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alba_back.settings')

import django
django.setup()
from whiskyouaway.models import Category, Event, CategoryContainer

def populate():

	music_pages = [
	{"title": "Trnsmt Festival",
	"url": "https://trnsmtfest.com/"},
	{"title": "King Tut's Wah Wah Hut",
	"url": "https://www.kingtuts.co.uk/"},
	{"title": "Tartan Heart Festival",
	"url": "https://tartanheartfestival.co.uk/"} ]

	cats = {"Music": {"events": music_pages}, } 

	for cat, cat_data in cats.items():
		c = add_cat(cat)
		for e in cat_data["events"]:
			add_event(c, e["title"], e["url"])

	# print the added categories

	for c in Category.objects.all():
		for e in Event.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(e)))

def add_event(cat, title, url, views=0):
	e = Event.objects.get_or_create(category=cat, title=title)[0]
	e.url=url
	e.views=views
	e.save()
	return e

def add_cat(name):
	c = Category.objects.get_or_create(name=name)[0]
	c.save()
	return c


if __name__ == '__main__':
	print("Starting Whisk You Away population script...")
	populate()