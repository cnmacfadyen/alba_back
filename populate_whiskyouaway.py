import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alba_back.settings')

import django
django.setup()
from whiskyouaway.models import Category, Event, CategoryContainer

def populate():

	animal_pages = [
	{"title": "Dog Jog Glasgow",
	"url": "/whiskyouaway/categories/animals/dog_jog/",
	"eurl": "http://www.whatsonglasgow.co.uk/events/pet/",
	"picture": "media/dog_jog.png"},
	{"title": "The Dog Lover Show",
	"url": "/whiskyouaway/categories/animals/dog_lover",
	"eurl": "http://www.whatsonglasgow.co.uk/events/pet/"},
	{"title": "Edinburgh Dog Show",
	"url": "/whiskyouaway/categories/animals/edinburgh_dogs/",
	"eurl": "http://www.whatsonglasgow.co.uk/events/pet/"},
	{"title": "Edinburgh Zoo", 
	"url": "/whiskyouaway/categories/animals/edinburgh_zoo/",
	"eurl": "https://www.edinburghzoo.org.uk/"},
	{"title": "Deep Sea World",
	"url": "/whiskyouaway/categories/animals/deep_sea_world/",
	"eurl": "https://www.deepseaworld.com/"},
	{"title": "Blair Drummond",
	"url": "/whiskyouaway/categories/animals/blair_drummond/",
	"eurl": "https://www.blairdrummond.com/"},
	{"title": "Highland Wildlife Park",
	"url": "/whiskyouaway/categories/animals/highland_wildlife/",
	"eurl": "http://www.highlandwildlifepark.org.uk/"},
	{"title": "Chihuahua Cafe",
	"url": "/whiskyouaway/categories/animals/chihuahua_cafe/",
	"eurl": "https://edinburghchihuahuacafe.co.uk/"},
	{"title": "Maison de Moggy - Scotland's First Cat Cafe",
	"url": "/whiskyouaway/categories/animals/cat_cafe/",
	"eurl": "https://www.maisondemoggy.com/"}
	]

	nightlife_pages = [
	{"title": "Blue Dog Cocktail Bar",
	"url": "/whiskyouaway/categories/nightlife/blue_dog/",
	"eurl": "https://www.bluedogglasgow.co.uk/"},
	{"title": "Tingle Shooter Bar",
	"url": "/whiskyouaway/categories/nightlife/tingle/",
	"eurl": "https://www.tinglebar.co.uk/"},
	{"title": "Firewater",
	"url": "/whiskyouaway/categories/nightlife/firewater/",
	"eurl": "https://en-gb.facebook.com/firewaterglasgowofficial/"},
	{"title": "Cathouse",
	"url": "/whiskyouaway/categories/nightlife/cathouse/",
	"eurl": "https://cathouse.co.uk/"},
	{"title": "Frankenstein",
	"url": "/whiskyouaway/categories/nightlife/frankenstein/",
	"eurl": "https://www.frankensteinedinburgh.co.uk/"},
	{"title": "Hive",
	"url": "/whiskyouaway/categories/nightlife/hive/",
	"eurl": "https://clubhive.co.uk/"}]

	sport_pages = [
	{"title": "European Athletics Indoor Championships, 2019",
	"url": "/whiskyouaway/categories/sport/indoor_athletics/",
	"eurl": "https://glasgow2019athletics.com"},
	{"title": "Guinness Pro14 Final, 2019",
	"url": "/whiskyouaway/categories/sport/pro14_final/",
	"eurl": "https://www.pro14rugby.org/final/"},
	{"title": "Blair Castle International Horse Trials",
	"url": "/whiskyouaway/categories/sport/horse_trials/",
	"eurl": "https://www.blairhorsetrials.co.uk"},
	{"title": "Solheim Cup, 2019",
	"url": "/whiskyouaway/categories/sport/solheim_cup/",
	"eurl": "https://solheimcup2019.com"},
	{"title": "Scottish Premiership",
	"url": "/whiskyouaway/categories/sport/spfl/",
	"eurl": "https://spfl.co.uk"},
	{"title": "Loch Lomond Water Ski Club",
	"url": "/whiskyouaway/categories/sport/water_ski/",
	"eurl": "http://www.lochlomondwaterskiclub.co.uk"},
	{"title": "Scotland's Boat Show",
	"url": "/whiskyouaway/categories/sport/boat_show/",
	"eurl": "http://www.scotlandsboatshow.co.uk"},
	{"title": "British Swimming Championships",
	"url": "/whiskyouaway/categories/sport/british_swimming/",
	"eurl": "https://www.britishswimming.org/events-and-tickets/british-swimming-championships-2019/"},
	{"title": "Premier League of Darts",
	"url": "/whiskyouaway/categories/sport/darts/",
	"eurl": "https://www.pdc.tv/tournament/unibet-premier-league"},
	{"title": "Cycling Track World Cup",
	"url": "/whiskyouaway/categories/sport/cycling_world_cup/",
	"eurl": "http://www.trackworldcup.co.uk"}
	]

	outdoor_pages = [
	{"title": "Military Tattoo",
	"url": "/whiskyouaway/categories/outdoors/tattoo/",
	"eurl": "www.edintattoo.co.uk"},
	{"title": "GlasGLOW",
	"url": "/whiskyouaway/categories/outdoors/glasglow/",
	"eurl": "http://www.whatsonglasgow.co.uk/event/064051-glasglow/"},
	{"title": "Highland Games",
	"url": "/whiskyouaway/categories/outdoors/highland_games/",
	"eurl": "http://www.shga.co.uk"},
	{"title": "Beltane Fire Festival",
	"url": "/whiskyouaway/categories/outdoors/fire_festival/",
	"eurl": "www.beltane.org"},
	{"title": "Scotland’s Big Nature Festival",
	"url": "/whiskyouaway/categories/outdoors/nature_festival/",
	"eurl": "www.ruralprojects.co.uk"},
	{"title": "Bard in the Botanics",
	"url": "/whiskyouaway/categories/outdoors/bard_botanics/",
	"eurl": "https://www.bardinthebotanics.co.uk"},
	{"title": "Outdoor Survival Courses",
	"url": "/whiskyouaway/categories/outdoors/outdoor_survival/",
	"eurl": "https://www.wildwoodbushcraft.com/scotland-courses?gclid=EAIaIQobChMIpKnBs-rU4AIVROR3Ch07qAOrEAAYAiAAEgK9Y_D_BwE"},
	{"title": "West Highland Way",
	"url": "/whiskyouaway/categories/outdoors/west_highland_way/",
	"eurl": "https://www.westhighlandway.org"},
	{"title": "Quadmania",
	"url": "/whiskyouaway/categories/outdoors/quadmania/",
	"eurl": "http://www.quadmaniascotland.co.uk"},
	{"title": "Outdoor Explore",
	"url": "/whiskyouaway/categories/outdoors/outdoor_explore/",
	"eurl": "https://www.outdoorexplore.co.uk"}
	]

	history_pages = [
	{"title": "Inveraray Castle",
	"url": "/whiskyouaway/categories/history/InverarayCastle/",
	"eurl": "https://www.zigzagonearth.com/inveraray-castle-scotland/"},
	{"title": "Dunrobin Castle",
	"url": "/whiskyouaway/categories/history/DunrobinCastle/",
	"eurl": "https://www.zigzagonearth.com/dunrobin-castle-scotland/"},
	{"title": "Edinburgh Castle",
	"url": "/whiskyouaway/categories/history/EdinburghCastle/",
	"eurl": "https://www.zigzagonearth.com/visit-edinburgh-castle-scotland/"},
	{"title": "Stirling Castle",
	"url": "/whiskyouaway/categories/history/StirlingCastle/",
	"eurl": "https://www.stirlingcastle.scot"},
	{"title": "Eilean Donan Castle",
	"url": "/whiskyouaway/categories/history/EileanDonanCastle/",
	"eurl": "https://www.zigzagonearth.com/eilean-donan-castle-scotland/"},
	{"title": "Kilchurn Castle",
	"url": "/whiskyouaway/categories/history/KilchurnCastle/",
	"eurl": "https://www.zigzagonearth.com/kilchurn-castle-loch-awe-scotland/"},
	{"title": "The Writers’ Museum ",
	"url": "/whiskyouaway/categories/history/WritersMuseum/",
	"eurl": "https://www.edinburghmuseums.org.uk/venue/writers-museum"},
	{"title": "Kelvingrove Art Gallery and Museum",
	"url": "/whiskyouaway/categories/history/KelvingroveMuseum/",
	"eurl": "https://www.glasgowlife.org.uk/museums/venues/kelvingrove-art-gallery-and-museum"},
	{"title": "National Museum of Scotland",
	"url": "/whiskyouaway/categories/history/NationalMuseums/",
	"eurl": "https://www.nms.ac.uk/national-museum-of-scotland/"},
	{"title": "V&A Dundee - Scotland’s first design museum ",
	"url": "/whiskyouaway/categories/history/VADundee/",
	"eurl": "https://www.vam.ac.uk/dundee"},
	{"title": "Riverside Museum, Glasgow ",
	"url": "/whiskyouaway/categories/history/RiversideMuseum/",
	"eurl": "https://www.glasgowlife.org.uk/museums/venues/riverside-museum)"}
	]

	family_pages = [
	{"title": "The Speyside Way, Cairngorms National Park",
	"url": "/whiskyouaway/categories/family/SpeysideWay/",
	"eurl": "https://cairngorms.co.uk"},
	{"title": "The Rob Roy Loop, Loch Lomond & The Trossachs National Park",
	"url": "/whiskyouaway/categories/family/RobRoyLoop/",
	"eurl": "https://www.lochlomond-trossachs.org/things-to-do/cycling/cycling-routes/rob-roy-loop/"},
	{"title": "Kelburn Castle near Largs, Ayrshire & Arran",
	"url": "/whiskyouaway/categories/family/KelburnCastle/",
	"eurl": "https://www.kelburnestate.com"},
	{"title": "Sea Kayak Oban",
	"url": "/whiskyouaway/categories/family/ObanKayak/",
	"eurl": "https://www.seakayakoban.com"},
	{"title": "Monikie Country Park",
	"url": "/whiskyouaway/categories/family/MonikiePark/",
	"eurl": "http://archive.angus.gov.uk/leisureaa/rangerservice/monikie.htm"}
	]

	music_pages = [
	{"title": "Trnsmt Festival",
	"url": "/whiskyouaway/categories/music/trnsmt/",
	"eurl": "https://trnsmtfest.com/"},
	{"title": "King Tut's Wah Wah Hut",
	"url": "/whiskyouaway/categories/music/king_tuts/",
	"eurl": "https://www.kingtuts.co.uk/"},
	{"title": "Belladrum Tartan Heart Festival",
	"url": "/whiskyouaway/categories/music/belladrum/",
	"eurl": "https://tartanheartfestival.co.uk/"},
	{"title": "The Islay Festival of Music and Malt",
	"url": "/whiskyouaway/categories/music/islay_music_and_malt/",
	"eurl": "https://www.islayfestival.com/"},
	{"title": "Summer Nights at The Bandstand",
	"url": "/whiskyouaway/categories/music/summer_nights/",
	"eurl": "https://www.ticketmaster.co.uk/Summer-Nights-tickets/artist/1992315"},
	{"title": "Stramash Live Music Bar",
	"url": "/whiskyouaway/categories/music/stramash_bar/",
	"eurl": "https://stramashedinburgh.com/"},
	{"title": "Burnsfest! 2019",
	"url": "/whiskyouaway/categories/music/burnsfest/",
	"eurl": "http://www.burnsfestival.com/burnsfest/"},
	{"title": "The Barrowland Ballroom",
	"url": "/whiskyouaway/categories/music/barrowlands/",
	"eurl": "http://barrowland-ballroom.co.uk/"},
	{"title": "Orkney Folk Festival",
	"url": "/whiskyouaway/categories/music/orkney_festival/",
	"eurl": "https://www.orkneyfolkfestival.com/"},
	{"title": "Crofter’s Music Bar",
	"url": "/whiskyouaway/categories/music/crofters/",
	"eurl": "https://croftersmusicbar.com/"}]


	food_pages = [
	{"title": "The Gin to My Tonic Show",
	"url": "/whiskyouaway/categories/food_and_drink/gin_to_my_tonic/",
	"eurl": "https://thegintomytonic.com/event/the-gin-to-my-tonic-show-glasgow-15th-17th-march-2019/"},
	{"title": "Scottish Vegan Festival",
	"url": "/whiskyouaway/categories/food_and_drink/vegan_festival/",
	"eurl": "https://www.vegfest.co.uk/event/scottish-vegan-festival-2/"},
	{"title": "Tennent’s Wellpark Brewery",
	"url": "/whiskyouaway/categories/food_and_drink/tennents_brewery/",
	"eurl": "http://www.tennentstours.com/"},
	{"title": "Foodies’ Festival",
	"url": "/whiskyouaway/categories/food_and_drink/foodies/",
	"eurl": "http://foodiesfestival.com/"},
	{"title": "Spirit of Speyside Whisky Festival",
	"url": "/whiskyouaway/categories/food_and_drink/speyside_whisky/",
	"eurl": "https://www.spiritofspeyside.com/"},
	{"title": "Tarbert Seafood Festival",
	"url": "/whiskyouaway/categories/food_and_drink/tarbert_seafood/",
	"eurl": "http://www.tarbertfestivals.co.uk/festival-seafood.php"},
	{"title": "Penicuik Market",
	"url": "/whiskyouaway/categories/food_and_drink/penicuik_market/",
	"eurl": "https://www.visitscotland.com/info/events/penicuik-market-p1598541"},
	{"title": "Autumn Fungi & Wild Food Foraging Walk",
	"url": "/whiskyouaway/categories/food_and_drink/autumn_fungi/",
	"eurl": "http://www.gallowaywildfoods.com/product/autumn_fungi_wild_food_foraging_walk_dumfries/"},
	{"title": "Highland Haggis Festival",
	"url": "/whiskyouaway/categories/food_and_drink/highland_haggis/",
	"eurl": "https://www.highlandhaggisfest.co.uk/"},
	{"title": "Highland Food & Drink Festival",
	"url": "/whiskyouaway/categories/food_and_drink/highland_food_drink/",
	"eurl": "https://www.eventbrite.co.uk/e/highland-food-drink-festival-tickets-53133201837"}
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

def add_event(cat, title, url):
	e = Event.objects.get_or_create(category=cat, title=title)[0]
	e.url=url
	e.save()
	return e

def add_cat(name):
	c = Category.objects.get_or_create(name=name)[0]
	c.save()
	return c


if __name__ == '__main__':
	print("Starting Whisk You Away population script...")
	populate()