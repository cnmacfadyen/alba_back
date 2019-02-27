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

	animal_pages = [
	{"title": "Dog Jog Glasgow",
	"url": "http://www.whatsonglasgow.co.uk/events/pet/"},
	{"title": "The Dog Lover Show",
	"url": "http://www.whatsonglasgow.co.uk/events/pet/"},
	{"title": "Edinburgh Dog Show",
	"url": "http://www.whatsonglasgow.co.uk/events/pet/"},
	{"title": "Edinburgh Zoo", 
	"url": "https://www.edinburghzoo.org.uk/"},
	{"title": "Deep Sea World",
	"url": "https://www.deepseaworld.com/"},
	{"title": "Blair Drummond",
	"url": "https://www.blairdrummond.com/"},
	{"title": "Highland Wildlife Park",
	"url": "http://www.highlandwildlifepark.org.uk/"},
	{"title": "Chihuahua Cafe",
	"url": "https://edinburghchihuahuacafe.co.uk/"},
	{"title": "Maison de Moggy - Scotland's First Cat Cafe",
	"url": "https://www.maisondemoggy.com/"}
	]

	nightlife_pages = [
	{"title": "Blue Dog Cocktail Bar", 
	"url": "https://www.bluedogglasgow.co.uk/"},
	{"title": "Tingle Shooter Bar",
	"url": "https://www.tinglebar.co.uk/"},
	{"title": "Firewater",
	"url": "https://en-gb.facebook.com/firewaterglasgowofficial/"},
	{"title": "Cathouse",
	"url": "https://cathouse.co.uk/"},
	{"title": "Frankenstein",
	"url": "https://www.frankensteinedinburgh.co.uk/"},
	{"title": "Hive",
	"url": "https://clubhive.co.uk/"}]


	cats = {"Music": {"events": music_pages},
	"Animals": {"events": animal_pages},
	'Nightlife': {"events": nightlife_pages} } 

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