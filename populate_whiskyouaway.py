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
	{"title": "https://tartanheartfestival.co.uk/"} ]


if __name__ == '__main__':
	print("Starting Whisk You Away population script...")
	populate()