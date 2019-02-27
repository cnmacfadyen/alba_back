import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alba_back.settings')

import django
django.setup()
from whiskyouaway.models import Category, Event, CategoryContainer

def populate():

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

	sport_pages = [
	{"title": "European Athletics Indoor Championships, 2019",
	"url": "https://glasgow2019athletics.com"},
	{"title": "Guinness Pro14 Final, 2019",
	"url": "https://www.pro14rugby.org/final/"},
	{"title": "Blair Castle International Horse Trials",
	"url": "https://www.blairhorsetrials.co.uk"},
	{"title": "Solheim Cup, 2019",
	"url": "https://solheimcup2019.com"},
	{"title": "Scottish Premiership",
	"url": "https://spfl.co.uk"},
	{"title": "Loch Lomond Water Ski Club",
	"url": "http://www.lochlomondwaterskiclub.co.uk"},
	{"title": "Scotland's Boat Show",
	"url": "http://www.scotlandsboatshow.co.uk"},
	{"title": "British Swimming Championships",
	"url": "https://www.britishswimming.org/events-and-tickets/british-swimming-championships-2019/"},
	{"title": "Premier League of Darts",
	"url": "https://www.pdc.tv/tournament/unibet-premier-league"},
	{"title": "Cycling Track World Cup",
	"url": "http://www.trackworldcup.co.uk"}
	]

	outdoor_pages = [
	{"title": "Military Tattoo",
	"url": "www.edintattoo.co.uk"},
	{"title": "GlasGLOW",
	"url": "http://www.whatsonglasgow.co.uk/event/064051-glasglow/"},
	{"title": "Highland Games",
	"url": "http://www.shga.co.uk"},
	{"title": "Beltane Fire Festival",
	"url": "www.beltane.org"},
	{"title": "Scotland’s Big Nature Festival",
	"url": "www.ruralprojects.co.uk"},
	{"title": "Bard in the Botanics",
	"url": "https://www.bardinthebotanics.co.uk"},
	{"title": "Outdoor Survival Courses",
	"url": "https://www.wildwoodbushcraft.com/scotland-courses?gclid=EAIaIQobChMIpKnBs-rU4AIVROR3Ch07qAOrEAAYAiAAEgK9Y_D_BwE"},
	{"title": "West Highland Way",
	"url": "https://www.westhighlandway.org"},
	{"title": "Quadmania",
	"url": "http://www.quadmaniascotland.co.uk"},
	{"title": "Outdoor Explore",
	"url": "https://www.outdoorexplore.co.uk"}
	]

	history_pages = [
	{"title": "Inveraray Castle",
	"url": "https://www.zigzagonearth.com/inveraray-castle-scotland/"},
	{"title": "Dunrobin Castle",
	"url": "https://www.zigzagonearth.com/dunrobin-castle-scotland/"},
	{"title": "Edinburgh Castle",
	"url": "https://www.zigzagonearth.com/visit-edinburgh-castle-scotland/"},
	{"title": "Stirling Castle",
	"url": "https://www.stirlingcastle.scot"},
	{"title": "Eilean Donan Castle",
	"url": "https://www.zigzagonearth.com/eilean-donan-castle-scotland/"},
	{"title": "Kilchurn Castle",
	"url": "https://www.zigzagonearth.com/kilchurn-castle-loch-awe-scotland/"},
	{"title": "The Writers’ Museum ",
	"url": "https://www.edinburghmuseums.org.uk/venue/writers-museum"},
	{"title": "Kelvingrove Art Gallery and Museum",
	"url": "https://www.glasgowlife.org.uk/museums/venues/kelvingrove-art-gallery-and-museum"},
	{"title": "National Museum of Scotland",
	"url": "https://www.nms.ac.uk/national-museum-of-scotland/"},
	{"title": "V&A Dundee - Scotland’s first design museum ",
	"url": "https://www.vam.ac.uk/dundee"},
	{"title": "Riverside Museum, Glasgow ",
	"url": "https://www.glasgowlife.org.uk/museums/venues/riverside-museum)"}
	]

	family_pages = [
	{"title": "The Speyside Way, Cairngorms National Park",
	"url": "https://cairngorms.co.uk"},
	{"title": "The Rob Roy Loop, Loch Lomond & The Trossachs National Park",
	"url": "https://www.lochlomond-trossachs.org/things-to-do/cycling/cycling-routes/rob-roy-loop/"},
	{"title": "Kelburn Castle near Largs, Ayrshire & Arran",
	"url": "https://www.kelburnestate.com"},
	{"title": "Sea Kayak Oban",
	"url": "https://www.seakayakoban.com"},
	{"title": "Monikie Country Park",
	"url": "http://archive.angus.gov.uk/leisureaa/rangerservice/monikie.htm"}
	]

	music_pages = [
	{"title": "Trnsmt Festival",
	"url": "https://trnsmtfest.com/"},
	{"title": "King Tut's Wah Wah Hut",
	"url": "https://www.kingtuts.co.uk/"},
	{"title": "Belladrum Tartan Heart Festival",
	"url": "https://tartanheartfestival.co.uk/"},
	{"title": "The Islay Festival of Music and Malt",
	"url": "https://www.islayfestival.com/"},
	{"title": "Summer Nights at The Bandstand",
	"url": "https://www.ticketmaster.co.uk/Summer-Nights-tickets/artist/1992315"},
	{"title": "Stramash Live Music Bar",
	"url": "https://stramashedinburgh.com/"},
	{"title": "Burnsfest! 2019",
	"url": "http://www.burnsfestival.com/burnsfest/"},
	{"title": "The Barrowland Ballroom",
	"url": "http://barrowland-ballroom.co.uk/"},
	{"title": "Orkney Folk Festival",
	"url": "https://www.orkneyfolkfestival.com/"},
	{"title": "Crofter’s Music Bar",
	"url": "https://croftersmusicbar.com/"}]


	food_pages = [
	{"title": "The Gin to My Tonic Show",
	"url": "https://thegintomytonic.com/event/the-gin-to-my-tonic-show-glasgow-15th-17th-march-2019/"},
	{"title": "Scottish Vegan Festival",
	"url": "https://www.vegfest.co.uk/event/scottish-vegan-festival-2/"},
	{"title": "Tennent’s Wellpark Brewery",
	"url": "http://www.tennentstours.com/"},
	{"title": "Foodies’ Festival",
	"url": "http://foodiesfestival.com/"},
	{"title": "Spirit of Speyside Whisky Festival",
	"url": "https://www.spiritofspeyside.com/"},
	{"title": "Tarbert Seafood Festival",
	"url": "http://www.tarbertfestivals.co.uk/festival-seafood.php"},
	{"title": "Penicuik Market",
	"url": "https://www.visitscotland.com/info/events/penicuik-market-p1598541"},
	{"title": "Autumn Fungi & Wild Food Foraging Walk",
	"url": "http://www.gallowaywildfoods.com/product/autumn-fungi-wild-food-foraging-walk-dumfries/"},
	{"title": "Highland Haggis Festival",
	"url": "https://www.highlandhaggisfest.co.uk/"},
	{"title": "Highland Food & Drink Festival",
	"url": "https://www.eventbrite.co.uk/e/highland-food-drink-festival-tickets-53133201837"}
	]

	cats = {"Music": {"events": music_pages},
	"Animals": {"events": animal_pages},
	'Nightlife': {"events": nightlife_pages},
	"Sport":{"events": sport_pages},
	"Outdoors":{"events": outdoor_pages}, 
	"History": {"events": history_pages}, 
	"Family": {"events": family_pages},
	"Food and Drink": {"events": food_pages}} 

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