import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alba_back.settings')

import django
django.setup()
from whiskyouaway.models import Category, Event, Advert, Categories, Events

def populate():

	animal_pages = [
	{"title": "Dog Jog Glasgow",
	"url": "/whiskyouaway/categories/animals/dog_jog/",
	"eurl": "http://www.whatsonglasgow.co.uk/events/pet/",
	"image":"static/images/animals/dog_jog.jpg"},
	{"title": "The Dog Lover Show",
	"url": "/whiskyouaway/categories/animals/dog_lover",
	"eurl": "http://www.whatsonglasgow.co.uk/events/pet/",
	"image":"static/images/animals/dog_lover.jpg"},
	{"title": "Edinburgh Dog Show",
	"url": "/whiskyouaway/categories/animals/edinburgh_dogs/",
	"eurl": "http://www.whatsonglasgow.co.uk/events/pet/",
	"image":"static/images/animals/edinburgh_dogs.jpg"},
	{"title": "Edinburgh Zoo", 
	"url": "/whiskyouaway/categories/animals/edinburgh_zoo/",
	"eurl": "https://www.edinburghzoo.org.uk/",
	"image":"static/images/animals/edinburgh_zoo.jpg"},
	{"title": "Deep Sea World",
	"url": "/whiskyouaway/categories/animals/deep_sea_world/",
	"eurl": "https://www.deepseaworld.com/",
	"image":"static/images/animals/deep_sea_world.jpg"},
	{"title": "Blair Drummond",
	"url": "/whiskyouaway/categories/animals/blair_drummond/",
	"eurl": "https://www.blairdrummond.com/",
	"image":"static/images/animals/blair_drummond.jpg"},
	{"title": "Highland Wildlife Park",
	"url": "/whiskyouaway/categories/animals/highland_wildlife/",
	"eurl": "http://www.highlandwildlifepark.org.uk/",
	"image":"static/images/animals/highland_wildlife.jpg"},
	{"title": "Chihuahua Cafe",
	"url": "/whiskyouaway/categories/animals/chihuahua_cafe/",
	"eurl": "https://edinburghchihuahuacafe.co.uk/",
	"image":"static/images/animals/chihuahua_cafe.jpg"},
	{"title": "Maison de Moggy - Scotland's First Cat Cafe",
	"url": "/whiskyouaway/categories/animals/cat_cafe/",
	"eurl": "https://www.maisondemoggy.com/",
	"image":"static/images/animals/cat_cafe.jpg"}
	]

	nightlife_pages = [
	{"title": "Blue Dog Cocktail Bar",
	"url": "/whiskyouaway/categories/nightlife/blue_dog/",
	"eurl": "https://www.bluedogglasgow.co.uk/",
	"image":"static/images/nightlife/blue_dog.jpg"},
	{"title": "Tingle Shooter Bar",
	"url": "/whiskyouaway/categories/nightlife/tingle/",
	"eurl": "https://www.tinglebar.co.uk/",
	"image":"static/images/nightlife/tingle.jpg"},
	{"title": "Firewater",
	"url": "/whiskyouaway/categories/nightlife/firewater/",
	"eurl": "https://en-gb.facebook.com/firewaterglasgowofficial/",
	"image":"static/images/nightlife/firewater.jpg"},
	{"title": "Cathouse",
	"url": "/whiskyouaway/categories/nightlife/cathouse/",
	"eurl": "https://cathouse.co.uk/",
	"image":"static/images/nightlife/cathouse.jpg"},
	{"title": "Frankenstein",
	"url": "/whiskyouaway/categories/nightlife/frankenstein/",
	"eurl": "https://www.frankensteinedinburgh.co.uk/",
	"image":"static/images/nightlife/frankenstein.jpg"},
	{"title": "Hive",
	"url": "/whiskyouaway/categories/nightlife/hive/",
	"eurl": "https://clubhive.co.uk/",
	"image":"static/images/nightlife/hive.jpg"}]

	sport_pages = [
	{"title": "European Athletics Indoor Championships, 2019",
	"url": "/whiskyouaway/categories/sport/indoor_athletics/",
	"eurl": "https://glasgow2019athletics.com",
	"image":"static/images/sport/indoor_athletics.jpg"},
	{"title": "Guinness Pro14 Final, 2019",
	"url": "/whiskyouaway/categories/sport/pro14_final/",
	"eurl": "https://www.pro14rugby.org/final/",
	"image":"static/images/sport/pro14_final.jpg"},
	{"title": "Blair Castle International Horse Trials",
	"url": "/whiskyouaway/categories/sport/horse_trials/",
	"eurl": "https://www.blairhorsetrials.co.uk",
	"image":"static/images/sport/horse_trials.jpg"},
	{"title": "Solheim Cup, 2019",
	"url": "/whiskyouaway/categories/sport/solheim_cup/",
	"eurl": "https://solheimcup2019.com",
	"image":"static/images/sport/solheim_cup.jpg"},
	{"title": "Scottish Premiership",
	"url": "/whiskyouaway/categories/sport/spfl/",
	"eurl": "https://spfl.co.uk",
	"image":"static/images/sport/spfl.jpg"},
	{"title": "Loch Lomond Water Ski Club",
	"url": "/whiskyouaway/categories/sport/water_ski/",
	"eurl": "http://www.lochlomondwaterskiclub.co.uk",
	"image":"static/images/sport/water_ski.jpg"},
	{"title": "Scotland's Boat Show",
	"url": "/whiskyouaway/categories/sport/boat_show/",
	"eurl": "http://www.scotlandsboatshow.co.uk",
	"image":"static/images/sport/boat_show.jpg"},
	{"title": "British Swimming Championships",
	"url": "/whiskyouaway/categories/sport/british_swimming/",
	"eurl": "https://www.britishswimming.org/events-and-tickets/british-swimming-championships-2019/",
	"image":"static/images/sport/british_swimming.jpg"},
	{"title": "Premier League of Darts",
	"url": "/whiskyouaway/categories/sport/darts/",
	"eurl": "https://www.pdc.tv/tournament/unibet-premier-league",
	"image":"static/images/sport/darts.jpg"},
	{"title": "Cycling Track World Cup",
	"url": "/whiskyouaway/categories/sport/cycling_world_cup/",
	"eurl": "http://www.trackworldcup.co.uk",
	"image":"static/images/sport/cycling_world_cup.jpg"}
	]

	outdoor_pages = [
	{"title": "Military Tattoo",
	"url": "/whiskyouaway/categories/outdoors/tattoo/",
	"eurl": "www.edintattoo.co.uk",
	"image":"static/images/outdoors/tattoo.jpg"},
	{"title": "GlasGLOW",
	"url": "/whiskyouaway/categories/outdoors/glasglow/",
	"eurl": "http://www.whatsonglasgow.co.uk/event/064051-glasglow/",
	"image":"static/images/outdoors/glasglow.jpg"},
	{"title": "Highland Games",
	"url": "/whiskyouaway/categories/outdoors/highland_games/",
	"eurl": "http://www.shga.co.uk",
	"image":"static/images/outdoors/highland_games.jpg"},
	{"title": "Beltane Fire Festival",
	"url": "/whiskyouaway/categories/outdoors/fire_festival/",
	"eurl": "www.beltane.org",
	"image":"static/images/outdoors/fire_festival.jpg"},
	{"title": "Scotland’s Big Nature Festival",
	"url": "/whiskyouaway/categories/outdoors/nature_festival/",
	"eurl": "www.ruralprojects.co.uk",
	"image":"static/images/outdoors/nature_festival.jpg"},
	{"title": "Bard in the Botanics",
	"url": "/whiskyouaway/categories/outdoors/bard_botanics/",
	"eurl": "https://www.bardinthebotanics.co.uk",
	"image":"static/images/outdoors/bard_botanics.jpg"},
	{"title": "Outdoor Survival Courses",
	"url": "/whiskyouaway/categories/outdoors/outdoor_survival/",
	"eurl": "https://www.wildwoodbushcraft.com/scotland-courses?gclid=EAIaIQobChMIpKnBs-rU4AIVROR3Ch07qAOrEAAYAiAAEgK9Y_D_BwE",
	"image":"static/images/outdoors/outdoor_survival.jpg"},
	{"title": "West Highland Way",
	"url": "/whiskyouaway/categories/outdoors/west_highland_way/",
	"eurl": "https://www.westhighlandway.org",
	"image":"static/images/outdoors/west_highland_way.jpg"},
	{"title": "Quadmania",
	"url": "/whiskyouaway/categories/outdoors/quadmania/",
	"eurl": "http://www.quadmaniascotland.co.uk",
	"image":"static/images/outdoors/quadmania.jpg"},
	{"title": "Outdoor Explore",
	"url": "/whiskyouaway/categories/outdoors/outdoor_explore/",
	"eurl": "https://www.outdoorexplore.co.uk",
	"image":"static/images/outdoors/outdoor_explore.jpg"}
	]

	history_pages = [
	{"title": "Inveraray Castle",
	"url": "/whiskyouaway/categories/history/InverarayCastle/",
	"eurl": "https://www.zigzagonearth.com/inveraray-castle-scotland/",
	"image":"static/images/history/InverarrayCastle.jpg"},
	{"title": "Dunrobin Castle",
	"url": "/whiskyouaway/categories/history/DunrobinCastle/",
	"eurl": "https://www.zigzagonearth.com/dunrobin-castle-scotland/",
	"image":"static/images/history/DunrobinCastle.jpg"},
	{"title": "Edinburgh Castle",
	"url": "/whiskyouaway/categories/history/EdinburghCastle/",
	"eurl": "https://www.zigzagonearth.com/visit-edinburgh-castle-scotland/",
	"image":"static/images/history/EdinburghCastle.jpg"},
	{"title": "Stirling Castle",
	"url": "/whiskyouaway/categories/history/StirlingCastle/",
	"eurl": "https://www.stirlingcastle.scot",
	"image":"static/images/history/StirlingCastle.jpg"},
	{"title": "Eilean Donan Castle",
	"url": "/whiskyouaway/categories/history/EileanDonanCastle/",
	"eurl": "https://www.zigzagonearth.com/eilean-donan-castle-scotland/",
	"image":"static/images/history/EilanDonanCastle.jpg"},
	{"title": "Kilchurn Castle",
	"url": "/whiskyouaway/categories/history/KilchurnCastle/",
	"eurl": "https://www.zigzagonearth.com/kilchurn-castle-loch-awe-scotland/",
	"image":"static/images/history/KilchurnCastle.jpg"},
	{"title": "The Writers’ Museum ",
	"url": "/whiskyouaway/categories/history/WritersMuseum/",
	"eurl": "https://www.edinburghmuseums.org.uk/venue/writers-museum",
	"image":"static/images/history/WritersMuseum.jpg"},
	{"title": "Kelvingrove Art Gallery and Museum",
	"url": "/whiskyouaway/categories/history/KelvingroveMuseum/",
	"eurl": "https://www.glasgowlife.org.uk/museums/venues/kelvingrove-art-gallery-and-museum",
	"image":"static/images/history/KelvingroveMuseum.jpg"},
	{"title": "National Museum of Scotland",
	"url": "/whiskyouaway/categories/history/NationalMuseums/",
	"eurl": "https://www.nms.ac.uk/national-museum-of-scotland/",
	"image":"static/images/history/NationalMuseums.jpg"},
	{"title": "V&A Dundee - Scotland’s first design museum ",
	"url": "/whiskyouaway/categories/history/VADundee/",
	"eurl": "https://www.vam.ac.uk/dundee",
	"image":"static/images/history/VADundee.jpg"},
	{"title": "Riverside Museum, Glasgow ",
	"url": "/whiskyouaway/categories/history/RiversideMuseum/",
	"eurl": "https://www.glasgowlife.org.uk/museums/venues/riverside-museum)",
	"image":"static/images/history/RiversideMuseum.jpg"}
	]

	family_pages = [
	{"title": "The Speyside Way, Cairngorms National Park",
	"url": "/whiskyouaway/categories/family/SpeysideWay/",
	"eurl": "https://cairngorms.co.uk",
	"image":"static/images/family/SpeysideWay.jpg"},
	{"title": "The Rob Roy Loop, Loch Lomond & The Trossachs National Park",
	"url": "/whiskyouaway/categories/family/RobRoyLoop/",
	"eurl": "https://www.lochlomond-trossachs.org/things-to-do/cycling/cycling-routes/rob-roy-loop/",
	"image":"static/images/family/RobRoyLoop.jpg"},
	{"title": "Kelburn Castle near Largs, Ayrshire & Arran",
	"url": "/whiskyouaway/categories/family/KelburnCastle/",
	"eurl": "https://www.kelburnestate.com",
	"image":"static/images/family/KelburnCastle.jpg"},
	{"title": "Sea Kayak Oban",
	"url": "/whiskyouaway/categories/family/ObanKayak/",
	"eurl": "https://www.seakayakoban.com",
	"image":"static/images/family/ObanKayak.jpg"},
	{"title": "Monikie Country Park",
	"url": "/whiskyouaway/categories/family/MonikiePark/",
	"eurl": "http://archive.angus.gov.uk/leisureaa/rangerservice/monikie.htm",
	"image":"static/images/family/MonikiePark.jpg"}
	]

	music_pages = [
	{"title": "Trnsmt Festival",
	"url": "/whiskyouaway/categories/music/trnsmt/",
	"eurl": "https://trnsmtfest.com/",
	"image":"static/images/music/trnsmt.jpg"},
	{"title": "King Tut's Wah Wah Hut",
	"url": "/whiskyouaway/categories/music/king_tuts/",
	"eurl": "https://www.kingtuts.co.uk/",
	"image":"static/images/music/king_tuts.jpg"},
	{"title": "Belladrum Tartan Heart Festival",
	"url": "/whiskyouaway/categories/music/belladrum/",
	"eurl": "https://tartanheartfestival.co.uk/",
	"image":"static/images/music/belladrum.jpg"},
	{"title": "The Islay Festival of Music and Malt",
	"url": "/whiskyouaway/categories/music/islay_music_and_malt/",
	"eurl": "https://www.islayfestival.com/",
	"image":"static/images/music/islay_festival.jpg"},
	{"title": "Summer Nights at The Bandstand",
	"url": "/whiskyouaway/categories/music/summer_nights/",
	"eurl": "https://www.ticketmaster.co.uk/Summer-Nights-tickets/artist/1992315",
	"image":"static/images/music/summer_nights.jpg"},
	{"title": "Stramash Live Music Bar",
	"url": "/whiskyouaway/categories/music/stramash_bar/",
	"eurl": "https://stramashedinburgh.com/",
	"image":"static/images/music/stramash.jpg"},
	{"title": "Burnsfest! 2019",
	"url": "/whiskyouaway/categories/music/burnsfest/",
	"eurl": "http://www.burnsfestival.com/burnsfest/",
	"image":"static/images/music/burnsfest.jpg"},
	{"title": "The Barrowland Ballroom",
	"url": "/whiskyouaway/categories/music/barrowlands/",
	"eurl": "http://barrowland-ballroom.co.uk/",
	"image":"static/images/music/barrowland_ballroom.jpg"},
	{"title": "Orkney Folk Festival",
	"url": "/whiskyouaway/categories/music/orkney_festival/",
	"eurl": "https://www.orkneyfolkfestival.com/",
	"image":"static/images/music/orkney_folk_festival.jpg"},
	{"title": "Crofter’s Music Bar",
	"url": "/whiskyouaway/categories/music/crofters/",
	"eurl": "https://croftersmusicbar.com/",
	"image":"static/images/music/crofters.jpg"}]


	food_pages = [
	{"title": "The Gin to My Tonic Show",
	"url": "/whiskyouaway/categories/food_and_drink/gin_to_my_tonic/",
	"eurl": "https://thegintomytonic.com/event/the-gin-to-my-tonic-show-glasgow-15th-17th-march-2019/",
	"image":"static/images/food/gin_to_my_tonic.jpg"},
	{"title": "Scottish Vegan Festival",
	"url": "/whiskyouaway/categories/food_and_drink/vegan_festival/",
	"eurl": "https://www.vegfest.co.uk/event/scottish-vegan-festival-2/",
	"image":"static/images/food/vegan_festival.jpg"},
	{"title": "Tennent’s Wellpark Brewery",
	"url": "/whiskyouaway/categories/food_and_drink/tennents_brewery/",
	"eurl": "http://www.tennentstours.com/",
	"image":"static/images/food/tennents_brewery.jpg"},
	{"title": "Foodies’ Festival",
	"url": "/whiskyouaway/categories/food_and_drink/foodies/",
	"eurl": "http://foodiesfestival.com/",
	"image":"static/images/foodfoodies_festival.jpg"},
	{"title": "Spirit of Speyside Whisky Festival",
	"url": "/whiskyouaway/categories/food_and_drink/speyside_whisky/",
	"eurl": "https://www.spiritofspeyside.com/",
	"image":"static/images/food/spirit_of_speyside.jpg"},
	{"title": "Tarbert Seafood Festival",
	"url": "/whiskyouaway/categories/food_and_drink/tarbert_seafood/",
	"eurl": "http://www.tarbertfestivals.co.uk/festival-seafood.php",
	"image":"static/images/food/tarbert_seafood_festival.jpg"},
	{"title": "Penicuik Market",
	"url": "/whiskyouaway/categories/food_and_drink/penicuik_market/",
	"eurl": "https://www.visitscotland.com/info/events/penicuik-market-p1598541",
	"image":"static/images/food/penicuik_market.jpg"},
	{"title": "Autumn Fungi & Wild Food Foraging Walk",
	"url": "/whiskyouaway/categories/food_and_drink/autumn_fungi/",
	"eurl": "http://www.gallowaywildfoods.com/product/autumn_fungi_wild_food_foraging_walk_dumfries/",
	"image":"static/images/food/autumn_fungi_walk.jpg"},
	{"title": "Highland Haggis Festival",
	"url": "/whiskyouaway/categories/food_and_drink/highland_haggis/",
	"eurl": "https://www.highlandhaggisfest.co.uk/",
	"image":"static/images/food/highland_haggis_festival.jpg"},
	{"title": "Highland Food & Drink Festival",
	"url": "/whiskyouaway/categories/food_and_drink/highland_food_drink/",
	"eurl": "https://www.eventbrite.co.uk/e/highland-food-drink-festival-tickets-53133201837",
	"image":"static/images/food/highland_food_and_drink_festival.jpg"}
	]

	adverts = [
	{"advertText": "Hi! I’ve come travelling to Scotland from Indonesia and I am looking to go and visit some historical sites, but it would be good to have someone come with me. I am in Scotland until the end of April 2019. Would anyone be interested in going to visit Stirling Castle? If not Stirling Castle, I’d be happy to visit another one. Email me if you’re interested. Thanks, Lia.",
	"email": "lia@example.com"},

	{"advertText": "Hi guys,I am really up for going to Quadmania, but my friends don’t want to go with me. Anyone interested in joining? Drop me an email if you fancy it. Let me know, Jill",
	"email": "jill@example.com"},

	{"advertText": "I love whisky, do you love whisky? I’m arranging a group trip to the Spirit of Speyside Whisky Festival. There will be a bus leaving from the Botanic Gardens in Glasgow at 8.30am on the 4th of May. We still have a few seats available, so sign up fast if you don’t want to miss out. Hamish",
	"email": "hamish@example.com"},

	{"advertText": "Hi, I’m a huge fan of Oasis and was really excited to book some tickets for a gig at King Tuts, where they were discovered, while I spend some time in Scotland. Sadly, my friend who was supposed to come with me can no longer make it, so I have a spare ticket. It’s yours for the value price. Drop me a line if you’re interested. The ticket is for Alice Merton on the 22nd of March. Cheers, Olivia.",
	"email": "olivia@example.com"},

	{"advertText":"Hey, I’m embarking on a challenge to attend a live match in each of Europe’s top football leagues. I’ve ticked off five countries so far and Scotland is next on my list. If anyone has any recommendations about what teams are the best to watch in Scotland and how I should plan my trip, please let me know. I don’t mind what teams I see play, just hoping that there’s a good atmosphere, but obviously the quality of the stadium’s pies is obviously going an important factor as well! I’d really appreciate any advice you can give me. Thanks, Sven.",
	"email":"sven@example.com"},

	{"advertText":"Hello, I am travelling to Scotland to try to take on the West Highland Way! Very excited about the challenge and the beautiful scenery I’m sure to see. I’m going to be starting on the 14th of June, and I’ll hopefully be finished within the week. Anyone else planning to do the hike around then? If so, let me know. It’d be good to get to know you beforehand. Thank you, Petra.",
	"email":"petra@example.com"},

	{"advertText":"Hi everyone, I’m looking to get a group together to do the Dog Jog in Glasgow to raise some money for the RSPCA. Anyone interested in joining? Drop me an email if you are! Thanks, Jenny",
	"email":"jenny@example.com"},

	{"advertText":"Hey! A few friends and I from Italy are spending some time in Glasgow and are planning to have a wild night out after watching Zebre play Glasgow Warriors. We always feel that the bigger the crowd, the greater the night, so please come and join us! We’re going to be starting our night in Firewater, and from there, who knows?! Let us know, Matteo.",
	"email":"matteo@example.com"},

	{"advertText":"Hello, My family and I are travelling up to Scotland from Cardiff for an adventure-packed holiday. We’d love to meet other families with similar interests to go on trips with us! First adventure on our list is kayaking in Oban! If you and your family are in and around the Oban area between the 15th and the 28th of July, let us know. Happy travelling, everyone. Richard.",
	"email":"richard@example.com"},

	{"advertText":"I consider myself a foodie, so I’m incredibly excited to be attending the Foodies Festival in Edinburgh this August. I’m going to be travelling down from Aberdeen, so was wondering if there was anyone else heading down from around this area so we could arrange a lift. Let me know, Bianca.",
	"email":"bianca@example.com"}
	]

	categories = [
	{"name": "Animals",
		
		 "image": "static/animals/edinburgh_zoo.jpg",
		
		 },
		{"name": "Family",

		 "image": "static/fish_images/mackerel.jpg",
 
		 },
		{"name": "Food",
		
		 "image": "static/fish_images/seabass.jpg",
	   
		 },
		{"name": "History",
		
		 "image": "static/fish_images/seabream.jpg",
	
		 },
		{"name": "Music",
		
		 "image": "static/fish_images/oyster.jpg",
  
		 },
		{"name": "Nightlife",

		 "image": "static/fish_images/mussels.jpg",
	   
		 },
		{"name": "Outdoors",
 
		 "image": "static/fish_images/brill.jpg",
   
		 },
 
		{"name": "Sport",
	  
		 "image": "static/fish_images/salmon.jpg",

		 },

	]

	events = [
		{
		"name": "Dog Jog",
		"description": "Looking to get fit and spend time with your dog? Dog Jog helps you to raise money for others, get fit and spend time with your canine buddy. What's not to love?! For more information, check out the link below.",
		# "ingredients": "Vegetable oil, for frying\n 1/4 red cabbage, thinly sliced (about 1 1/2 cups)\n 1/2 cup fresh cilantro, roughly chopped\nJuice of 1 lime, plus wedges for serving\n2 tablespoons honey or agave nectar\n1/2 cup mayonnaise\nKosher salt\n12 corn tortillas\n3/4 cup all-purpose flour\n1/2 teaspoon chili powder\nFreshly ground pepper\n1 1/4 pounds skinless halibut fillet, cut into 2-by-1/2-inch pieces\n1 Hass avocado\n1/2 cup fresh salsa",
		# "method": "Heat about 3 inches vegetable oil in a medium pot over medium-low heat until a deep-fry thermometer registers 375 degrees F. Meanwhile, toss the cabbage, cilantro, lime juice, honey and mayonnaise in a bowl. Season the slaw with salt.\nWarm the tortillas in a skillet over medium-low heat or wrap in a damp cloth and microwave 25 seconds. Wrap in a towel to keep warm.\nMix the flour, chili powder, and salt and pepper to taste in a shallow bowl. Dredge the fish in the flour mixture, then fry in batches until golden and just cooked through, 2 to 3 minutes. Transfer with a slotted spoon to a paper-towel-lined plate to drain. Season with salt.\nHalve, pit and slice the avocado. Fill the tortillas with the fish, avocado, slaw and salsa. Serve with lime wedges.",
		"categories": "Animals",
		# "time": 20,
		# "serves": 4,
		"image": "dog_jog.jpg",
		"user": "Admin",
		"url": "https://www.dogjog.co.uk/glasgow/",
		},
		{
			"name": "TRNSMT",
			"description": "TRNSMT is Scotland's newest, most exciting festival. Returning in 2019 with a cracking line-up including George Ezra, Stormzy and Years & Years, this year's festival is not to be missed!",
			# "ingredients": "450g (1lb) skinless fish fillets (salmon, haddock, etc) cut into chunks, 4 spring onions finely sliced, 1 red chilli, deseeded and finely chopped, 2 tbsp Thai Taste Red Curry Paste, 2 tbsp fresh coriander leaves, 1 tbsp Thai Taste Palm Sugar, 1 tsp Thai Taste Fish Sauce, 1 tbsp fresh lime juice, 50g (2oz) fine green beans, finely sliced, 1 tbsp Thai Taste Rice Bran Oil, for frying",
			# "method": "1. Place the fish chunks, spring onions, chilli, curry paste, coriander, palm sugar, fish sauce, lime juice and a pinch of salt in a food processor and blend until finely minced. 2. Transfer to a bowl and stir in the sliced green beans. 3. Divide the mixture into 16 pieces, roll each one into a ball and then flatten into discs. 4. Transfer the fish cakes to a plate, cover with cling film and place in the fridge for 30 minutes to 1 hour to firm up. 5. Heat the oil in a large frying pan and when very hot fry the fish cakes for about 1-2 minute each side, until golden brown and cooked through. Lift out and drain on kitchen paper, then serve with a selection of dipping sauces and a wedge of lime. Garnish with spring onions.",
			"categories": "Music",
			# "time": 40,
			# "serves": 4,
			"image": "trnsmt.jpg",
			"user": "Admin",
			"url": "https://trnsmtfest.com/",

		},
		{
			"name": "Premier League of Darts",
			"description": "The Premier League of Darts is well known for its lively atmosphere. For your chance to experience it in Aberdeen, click the link below.",
			# "ingredients": "1 pound tiny whole fish, such as blue anchovies, 1 tablespoon salt (finely ground), 1 cup flour (all-purpose), 1 to 2 cups oil for frying, 4 to 8 lemon wedges",
			# "method": "Pick through your fish to look for any that are not pristine. You are looking for ones where the bellies are torn open. This is from enzymes within the fish breaking it down. Toss these and use only those that look nice, smell a bit like cucumbers (not like nasty fish) and that have clear eyes. Mix the salt and flour well. Pour the oil into a cast-iron frying pan or other suitable pan and heat it to 350 F over medium heat. Dust the fish in the seasoned flour and then shake off the excess. Fry in batches, stirring them so they don't stick together, for 2 to 3 minutes. Drain on a fine-meshed rack or paper towels. If you are making a lot of them, heat the oven to warm and place the fish in the oven until you are ready to serve since it is important that you serve whitebait toasty hot.",
			"categories": "Sport",
			# "time": 15,
			# "serves": 4,
			"image": "darts.jpg",
			"user": "Admin",
			"url": "https://www.pdc.tv/tournament/unibet-premier-league"
		},

		{
			"name": "GlasGLOW",
			"description": "A light show like no other! Set against the beautiful backdrop of Glasgow's Botanic Gardens, GlasGLOW will awaken your senses and spark your imagination. To find out more, check out the link below.",
			# "ingredients": "250g puy lentils, 2 shallots, 4 tbsp olive oil, 140g shiitake mushrooms, 250g pack cherry or plum tomatoes, 2 tbsp capers, 150ml white wine, 4 x brill (or any other white fish like cod) fillets, skinned - about 140-175g/5-6oz each, 1 small lemon, 1 small bunch of flat-leaf parsley, 140g baby spinach",
			# "method": "Heat oven to 200C/fan oven 180C/gas mark 6. Tip the lentils into a pan, and cover with cold water. Bring to the boil and cook for 15-20 mins until they are tender. Drain and keep to one side. Fry the shallots in half the oil in a shallow roasting tray on top of the hob, until softened. Increase the heat and add the mushrooms. Cook for a couple of minutes, until they are colouring around the edges. Remove the tray from the heat, then stir in the cooked lentils, halved tomatoes, capers and wine. Sit the fish on the lentils then top with a couple of slices of lemon and drizzle over the remaining oil. Season everything with flaked sea salt and freshly ground black pepper. Roast for 15 mins – until the fish is cooked through and beginning to go golden on top. Gently lift fish from the tray. Stir the parsley and spinach into lentils, until the spinach starts to wilt. Spoon onto 4 plates, sit the fish on top and serve.",
			"categories": "Outdoors",
			# "time": 50,
			# "serves": 4,
			"image": "glasglow.jpg",
			"user": "Admin",
			"url": "https://www.itison.com/glasglow",

		},
			{
			"name": "Speyside Way",
			"description": "This 107 km route in the Scottish Highlands offers some of the most breathtaking scenery the country has to offer. Follow the river Spey from Aviemore to Buckie on this beautiful trail.",
			# "ingredients": "250g puy lentils, 2 shallots, 4 tbsp olive oil, 140g shiitake mushrooms, 250g pack cherry or plum tomatoes, 2 tbsp capers, 150ml white wine, 4 x brill (or any other white fish like cod) fillets, skinned - about 140-175g/5-6oz each, 1 small lemon, 1 small bunch of flat-leaf parsley, 140g baby spinach",
			# "method": "Heat oven to 200C/fan oven 180C/gas mark 6. Tip the lentils into a pan, and cover with cold water. Bring to the boil and cook for 15-20 mins until they are tender. Drain and keep to one side. Fry the shallots in half the oil in a shallow roasting tray on top of the hob, until softened. Increase the heat and add the mushrooms. Cook for a couple of minutes, until they are colouring around the edges. Remove the tray from the heat, then stir in the cooked lentils, halved tomatoes, capers and wine. Sit the fish on the lentils then top with a couple of slices of lemon and drizzle over the remaining oil. Season everything with flaked sea salt and freshly ground black pepper. Roast for 15 mins – until the fish is cooked through and beginning to go golden on top. Gently lift fish from the tray. Stir the parsley and spinach into lentils, until the spinach starts to wilt. Spoon onto 4 plates, sit the fish on top and serve.",
			"categories": "Family",
			# "time": 50,
			# "serves": 4,
			"image": "SpeysideWay.jpg",
			"user": "Admin",
			"url": "https://cairngorms.co.uk/", 

		}
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

	for item in adverts:
		a = add_ad(item["advertText"], item["email"])
		print(format(str(a)))

	for item in categories:
		f = add_categories(item["name"],item["image"])
		print(format(str(f)))


	for item in events:
		r = add_events(item["name"], item["description"], get_categories(item["categories"]), item["image"], item["user"], item["url"])
		print(format(str(r)))

def add_event(cat, title, url):
	e = Event.objects.get_or_create(category=cat, title=title)[0]
	e.url=url
	e.save()
	return e

def add_cat(name):
	c = Category.objects.get_or_create(name=name)[0]
	c.save()
	return c

def add_ad(advertText, email):
	a = Advert.objects.get_or_create(advertText=advertText, email=email)
	return a


def add_categories(name, image):
	f = Categories.objects.get_or_create(name = name, image = image)
	return f

def get_categories(name):
	categories = Categories.objects.get(name = name)
	return categories


def add_events(name, description, categories, image, user, url):
	r = Events.objects.get_or_create(name = name, description = description, categories = categories, image = image, user=user, url=url)
	return r


if __name__ == '__main__':
	print("Starting Whisk You Away population script...")
	populate()