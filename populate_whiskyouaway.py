import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alba_back.settings')

import django
django.setup()
from whiskyouaway.models import Category, Event, Advert, Categories, Events

def populate():

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
	
	 },
	{"name": "Family",

	 },
	{"name": "Food",
   
	 },
	{"name": "History",

	 },
	{"name": "Music",

	 },
	{"name": "Nightlife",
   
	 },
	{"name": "Outdoors",

	 },

	{"name": "Sport",

	}

	]

	events = [
	{
	"name": "Dog Jog",
	"likes": 43,
	"description": "Looking to get fit and spend time with your dog? Dog Jog helps you to raise money for others, get fit and spend time with your canine buddy. What's not to love?! For more information, check out the link below.",
	"categories": "Animals",
	"image": "dog_jog.png",
	"url": "https://www.dogjog.co.uk/glasgow/",
	},
	{
	"name": "The Dog Lover Show",
	"likes": 12,
	"description":"Do you love dogs? If so, then the Dog Lover's Show is the place for you to be. There are fun-filled displays and events from some of the most talented dogs in the UK on offer for the whole family to enjoy. To find out more, click on the link below.",
	"categories": "Animals",
	"image":"dog_lover.jpg",
	"url": "http://www.whatsonglasgow.co.uk/events/pet/"
	},
	{
	"name": "Edinburgh Dog Show",
	"likes": 3,
	"description":"The Scottish Kennel Club Dog Show is the place to go if you want to learn more about dogs. Bring your dog along so they can sample some of the treats on offer and cheer on the other dogs competing for Best in Show.",
	"categories": "Animals",
	"image":"edinburgh_dogs.jpg",
	"url": "http://www.whatsonglasgow.co.uk/events/pet/"
	},
	{
	"name": "Edinburgh Zoo", 
	"likes": 10,
	"description": "For an unforgettable day out, give Edinburgh Zoo a try. With world-class attractions and lots of different animals to see, any animal lover is sure to have a ball.",
	"categories": "Animals",
	"image":"edinburgh_zoo.jpg",
	"url": "https://www.edinburghzoo.org.uk/"
	},
	{
	"name": "Deep Sea World",
	"likes": 23,
	"description": "Fascinated by marine life? Go and visit Deep Sea World, Scotland's National Aquarium, to learn more about animals from the oceans. Or if you're brave enough, and old enough, you can try diving with sharks!",
	"categories": "Animals",
	"image":"deep_sea_world.jpg",
	"url": "https://www.deepseaworld.com/"
	},
	{
	"name": "Blair Drummond",
	"likes": 0,
	"description":"A safari park in Scotland! If exotic and rare animals is your thing, Blair Drummond Safari Park is the place to be. Spend the day here and you'll get the chance to meet Scotland's only giraffes and take a boat trip to Chimp Island. Find out more at the link below.",
	"categories": "Animals",
	"image":"blair_drummond.png",
	"url": "https://www.blairdrummond.com/"
	},
	{
	"name": "Highland Wildlife Park",
	"likes": 0,
	"description":"Want to see wildlife in a spectacular setting? Highland Wildlife Park is the place for you. With a diverse range of wildlife, from native species to animals from further afield, the Park offers you the chance to explore both in the car and on foot.",
	"categories": "Animals",
	"image":"highland_wildlife.jpg",
	"url": "http://www.highlandwildlifepark.org.uk/"
	},
	{"name": "Chihuahua Cafe",
	"likes": 0,
	"description":"Book a time to visit the Chihuahua Cafe and sample some food in the company of Chihuahuas!",
	"categories": "Animals",
	"image":"chihuahua_cafe.png",
	"url": "https://edinburghchihuahuacafe.co.uk/"
	},
	{"name": "Maison de Moggy - Scotland's First Cat Cafe",
	"likes": 0,
	"description":"If you love cats and cafés, then give Scotland's first ever cat café a try. Maison de Moggy offers a homey café experience with the added benefit of being able to relax in the company of furry friends. It can get busy, so be sure to make a booking using the link below to guarantee your spot.",
	"categories": "Animals",
	"image":"cat_cafe.jpg",
	"url": "https://www.maisondemoggy.com/"
	},

	{"name": "Blue Dog Cocktail Bar",
	"likes": 0,
	"description": "If you enjoy cocktails, Blue Dog is the place to go to in Glasgow. With live entertainment and an extensive drinks list, you're sure not to be disappointed.",
	"categories": "Nightlife",
	"image":"blue_dog.jpg",
	"url": "https://www.bluedogglasgow.co.uk/"
	},
	{"name": "Tingle Shooter Bar",
	"likes": 0,
	"description":"If you like to start off a night out with a shot, try Tingle Shooter Bar for a vibrant atmosphere and a plethora of shots to choose from.",
	"categories": "Nightlife",
	"image":"tingle.jpg",
	"url": "https://www.tinglebar.co.uk/"
	},
	{"name": "Firewater",
	"likes": 0,
	"description": "For a lively night in Glasgow, why not give Firewater a try? With good music and a lots of events on offer, there's something for everyone.",
	"categories": "Nightlife",
	"image":"firewater.jpg",
	"url": "https://en-gb.facebook.com/firewaterglasgowofficial/"
	},
	{"name": "Cathouse",
	"likes": 0,
	"description":"Not into mainstream music? That's okay, give the Cathouse a try. It's not just a typical rock club, with three rooms on offer, there's a wide mix of tunes on offer.",
	"categories": "Nightlife",
	"image": "cathouse.jpg",
	"url": "https://cathouse.co.uk/"
	},
	{"name": "Frankenstein",
	"likes": 0,
	"description": "For a fun and friendly pub in Edinburgh, try Frankenstein. Situated in  the heart of the Old Town, there's lots of food and drinks to try.",
	"categories": "Nightlife",
	"image":"frankenstein.jpg",
	"url": "https://www.frankensteinedinburgh.co.uk/"
	},
	{"name": "Hive",
	"likes": 0,
	"description":"For a student-orientated night out in Edinburgh, the Hive is the place to be. To book a VIP table, use the link below.",
	"categories": "Nightlife",
	"image": "hive.jpg",
	"url": "https://clubhive.co.uk/"
	},
	{
	"name": "European Athletics Indoor Championships, 2019",
	"likes": 0,
	"description": "This year, the 35th European Indoor Athletics Championships are taking place in Glasgow. For your chance to see over 600 top-class athletes from 50 nations compete for medals at the Emirates Arena, click on the link below.",
	"categories": "Sport",
	"image":"indoor_athletics.jpg",
	"url": "https://glasgow2019athletics.com"
	},
	{"name": "Guinness Pro14 Final, 2019",
	"likes": 0,
	"description":"This year, the world-renowned Guinness Pro 14 will reach its conclusion at Celtic Park. Glasgow Warriors and Edinburgh are still in the hunt, so there are other chances to catch some top tier rugby. To learn more, visit the link below.",
	"categories": "Sport",
	"image":"pro14_final.jpg",
	"url": "https://www.pro14rugby.org/final/"
	},
	{
	"name": "Blair Castle International Horse Trials",
	"likes": 0,
	"description":"If you love all things equestrian, then you should visit Scotland's premier equestrian event. Situated in the picturesque Atholl Estates and with both eventing and non-eventing competitions on offer, you'll definitely find something you enjoy.",
	"categories": "Sport",
	"image":"horse_trials.jpg",
	"url": "https://www.blairhorsetrials.co.uk"
	},
	{
	"name": "Solheim Cup, 2019",
	"likes": 0,
	"description":"Scotland is well-known for being the home of golf. This year, it is also home to the biggest event in women's golf! Watch Team Europe take on Team USA at Gleneagles this September. Who will take home the coveted trophy?",
	"categories": "Sport",
	"image":"solheim_cup.jpg",
	"url": "https://solheimcup2019.com"
	},
	{
	"name": "Scottish Premiership",
	"likes": 0,
	"description":"Scotland's recent football history may not be as illustrious as in previous years, but it remains a huge part of our culture and an experience not to be missed. Check out the link below to see what teams are in your area.",
	"categories": "Sport",
	"image":"spfl.jpg",
	"url": "https://spfl.co.uk"
	},
	{
	"name": "Loch Lomond Water Ski Club",
	"likes": 0,
	"description":"Learn how to water ski on the famous Loch Lomond!",
	"categories": "Sport",
	"image":"water_ski.jpg",
	"url": "http://www.lochlomondwaterskiclub.co.uk"
	},
	{
	"name": "Scotland's Boat Show",
	"likes": 0,
	"description":"With boats on SAIL, both pre-owned and brand-new, and a variety of exhibitors on offer, there's plenty on offer for a nautical enthusiast to enjoy.",
	"categories": "Sport",
	"image":"boat_show.png",
	"url": "http://www.scotlandsboatshow.co.uk",
	},
	{
	"name": "British Swimming Championships",
	"likes": 0,
	"description":"Watch the best swimmers Britain has to offer battle it out to be named British Champion in Glasgow this April.",
	"categories": "Sport",
	"image":"british_swimming.jpg",
	"url": "https://www.britishswimming.org/events-and-tickets/british-swimming-championships-2019/"
	},
	{
	"name": "Premier League of Darts",
	"likes": 0,
	"description": "The Premier League of Darts is well known for its lively atmosphere. For your chance to experience it in Aberdeen, click the link below.",
	"categories": "Sport",
	"image": "darts.jpg",
	"url": "https://www.pdc.tv/tournament/unibet-premier-league"
	},
	{
	"name": "Cycling Track World Cup",
	"likes": 0,
	"description":"This year, the second round of the Track Cycling World Cup series takes place at the Sir Chris Hoy Velodrome in Glasgow. Watch the best cyclists in the world on the journey to Tokyo 2020.",
	"categories": "Sport",
	"image":"cycling_world_cup.jpg",
	"url": "http://www.trackworldcup.co.uk"
	},
	{
	"name": "Military Tattoo",
	"likes": 0,
	"description":"A world-renowned event steeped in Scottish tradition, the Edinburgh Military Tattoo is an event not to be missed. Set against the beautiful backdrop of Edinburgh Castle experience this outdoor event like no other.",
	"categories": "Outdoors",
	"image":"tattoo.jpg",
	"url": "www.edintattoo.co.uk"
	},
	{
	"name": "GlasGLOW",
	"likes": 0,
	"description": "A light show like no other! Set against the beautiful backdrop of Glasgow's Botanic Gardens, GlasGLOW will awaken your senses and spark your imagination. To find out more, check out the link below.",
	"categories": "Outdoors",
	"image": "glasglow.jpg",
	"url": "https://www.itison.com/glasglow",
	},
	{
	"name": "Highland Games",
	"likes": 0,
	"description":"Experience an outdoor event steeped in Scottish tradition. Whether it's tossing the caber or haggis hurling, there's lots to see and enjoy. There are events held throughout the country, so check out the link below to find one near you.",
	"categories": "Outdoors",
	"image":"highland_games.jpg",
	"url": "http://www.shga.co.uk"
	},
	{
	"name": "Beltane Fire Festival",
	"likes": 0,
	"description":"For a modern interpritation of traditional a Celtic festival, head to the Beltane Fire Festival. There'll be fire, drumming and acrobatics galore!",
	"categories": "Outdoors",
	"image":"fire_festival.jpg",
	"url": "www.beltane.org"
	},
	{
	"name": "Scotland’s Big Nature Festival",
	"likes": 0,
	"description":"If you enjoy the occasional dabbling in time travel, why not check out Scotland's Big Nature Festival to learn more about nature in Scotland.",
	"categories": "Outdoors",
	"image":"nature_festival.jpg",
	"url": "www.ruralprojects.co.uk"
	},
	{
	"name": "Bard in the Botanics",
	"likes": 0,
	"description":"Bard in the Botanics is Scotland's Premier Shakespeare company. Every year, it performs a number of Shakespeare's plays in the beautiful surroundings of Glasgow's Botanic Gardens. Don't worry if it rains, they'll just head inside the Kibble Palace! To see what's on offer this year, check out the link below.",
	"categories": "Outdoors",
	"image":"bard_botanics.jpg",
	"url": "https://www.bardinthebotanics.co.uk"
	},
	{
	"name": "Outdoor Survival Courses",
	"likes": 0,
	"description":"Learn how to survive in Scotland's rugged landscape by taking a Wildwood Bushcraft course. Be it a nomadic coastal adventure or a foraging retreat, there's plenty to learn and to see.",
	"categories": "Outdoors",
	"image":"outdoor_survival.jpg",
	"url": "https://www.wildwoodbushcraft.com/scotland-courses?gclid=EAIaIQobChMIpKnBs-rU4AIVROR3Ch07qAOrEAAYAiAAEgK9Y_D_BwE"
	},
	{"name": "West Highland Way",
	"likes": 0,
	"description":"If you love hiking, the West Highland Way could be the route for you. Scotland is famed for its beautiful scenery, and one of the best ways to experience it is to take on the West Highland Way. The route begins in Milngavie and stretches 96 miles to Fort William, so there is plenty of varied scenery to experience on the way. There are hotels en route too, if camping isn't your scene! To find out more and plan out your trip, check out the link below.",
	"categories": "Outdoors",
	"image":"west_highland_way.jpg",
	"url": "https://www.westhighlandway.org"
	},
	{"name": "Quadmania",
	"likes": 0,
	"description":"For those seeking an outdoor adventure that gets the pulses racing, Quadmania is the perfect choice. Be it trekking by quad bike through woodland, farmland and forests, or clay shooting and archery, there's plenty on offer for everyone to enjoy!",
	"categories": "Outdoors",
	"image":"quadmania.jpg",
	"url": "http://www.quadmaniascotland.co.uk"
	},
	{"name": "Outdoor Explore",
	"likes": 0,
	"description":"Enjoy Scotland's beautiful outdoors whilst kayaking! What better way to get up close to nature? There are various locations available throughout the east coast of Scotland, so check out the link below to learn more.",
	"categories": "Outdoors",
	"image":"outdoor_explore.jpg",
	"url": "https://www.outdoorexplore.co.uk"
	},
	{
	"name": "Inveraray Castle",
	"likes": 0,
	"description":"Inveraray Castle, situated on the shores of Loch Fyne, is an example of early Gothic Revival architecture in Scotland. The castle is home to a 16-acre garden and a collection of over 1300 antique weapons. It is open to the public between April and October.",
	"categories": "History",
	"image":"InverarrayCastle.jpg",
	"url": "https://www.zigzagonearth.com/inveraray-castle-scotland/"
	},
	{
	"name": "Dunrobin Castle",
	"likes": 0,
	"description":"The largest house in Northern Scotland, Dunrobin Castle is the family seat of the Clan Sutherland. It dates back to the Middle Ages, with much of its current architecture dating to the 17th century. The castle and grounds are open to the public between April and October, offering falconry displays and tours.",
	"categories": "History",
	"image":"DunrobinCastle.jpg",
	"url": "https://www.zigzagonearth.com/dunrobin-castle-scotland/"
	},
	{
	"name": "Edinburgh Castle",
	"likes": 0,
	"description":"Edinburgh Castle is situated in the heart of Scotland's capital and has been occupied by royalty since at least the 12th century. It is Scotland's most visited tourist attraction, gaining over 2 million visitors in 2017! Perhaps its most iconic feature is the One o'clock Gun display which takes place daily except Sundays. Come and visit Scotland's most famous castle, open to the public all year round!",
	"categories": "History",
	"image":"EdinburghCastle.jpg",
	"url": "https://www.zigzagonearth.com/visit-edinburgh-castle-scotland/"
	},
	{
	"name": "Stirling Castle",
	"likes": 0,
	"description":"Stirling Castle is one of Scotland's largest and most historically important castles. Many famous historical figures have lived here including Mary Queen of Scots. The castle and grounds are open to the public all year round!",
	"categories": "History",
	"image":"StirlingCastle.jpg",
	"url": "https://www.stirlingcastle.scot"
	},
	{
	"name": "Eilean Donan Castle",
	"likes": 0,
	"description":"Come and visit Scotland's most recognisable castle in the heart of the West Highlands! Stunning landscapes surround this iconic landmark, and the grounds also house a visitor centre and cafe.",
	"categories": "History",
	"image":"EilanDonanCastle.jpg",
	"url": "https://www.zigzagonearth.com/eilean-donan-castle-scotland/",
	},
	{
	"name": "Kilchurn Castle",
	"likes": 0,
	"description":"The ruins of 15th century Kilchurn castle, nestled within the shores of stunning Loch Awe, are a must-see for any history buffs visiting Scotland. ",
	"categories": "History",
	"image":"KilchurnCastle.jpg",
	"url": "https://www.zigzagonearth.com/kilchurn-castle-loch-awe-scotland/"
	},
	{
	"name": "The Writers’ Museum ",
	"likes": 0,
	"description":"Any Scottish literature fans mustn't miss out on the chance to visit this attraction. The museum is a celebration of the lives of Robert Burns, Sir Walter Scott and Robert Louis Stevenson. Open daily from 10am - 5pm.",
	"categories": "History",
	"image":"WritersMuseum.jpg",
	"url": "https://www.edinburghmuseums.org.uk/venue/writers-museum"
	},
	{
	"name": "Kelvingrove Art Gallery and Museum",
	"likes": 0,
	"description":"Kelvingrove Museum, in the heart of Glasgow's west end, is a fantastic day out for all the family. Art, animals, science and much more are on display at Kelvingrove.",
	"categories": "History",
	"image":"KelvingroveMuseum.jpg",
	"url": "https://www.glasgowlife.org.uk/museums/venues/kelvingrove-art-gallery-and-museum"
	},
	{"name": "National Museum of Scotland",
	"likes": 0,
	"description":"There is somethong for everyone at the National Museum in Edinburgh, including science, technology, fashion and natural history.",
	"categories": "History",
	"image":"NationalMuseums.jpg",
	"url": "https://www.nms.ac.uk/national-museum-of-scotland/"
	},
	{"name": "V&A Dundee - Scotland’s first design museum ",
	"likes": 0,
	"description":"The V & A in Dundee is the first of its kind as Scotland's only design museum. Come and visit this museum to view quirky exhibits of fashion and artwork.",
	"categories": "History",
	"image":"VADundee.jpg",
	"url": "https://www.vam.ac.uk/dundee"
	},
	{
	"name": "Riverside Museum, Glasgow ",
	"likes": 0,
	"description":"The recently built, award-winning Riverside Museum takes you on a tour through the history of transport in Scotland. With interactive, modern and historical displays, there's sure to be something to please everyone at this museum.",
	"categories": "History",
	"image":"RiversideMuseum.jpg",
	"url": "https://www.glasgowlife.org.uk/museums/venues/riverside-museum)"
	},
	{
	"name": "Speyside Way",
	"likes": 0,
	"description": "This 107 km route in the Scottish Highlands offers some of the most breathtaking scenery the country has to offer. Follow the river Spey from Aviemore to Buckie on this beautiful trail.",
	"categories": "Family",
	"image": "SpeysideWay.jpg",
	"url": "https://cairngorms.co.uk/", 
	},
	{
	"name": "The Rob Roy Loop, Loch Lomond & The Trossachs National Park",
	"likes": 0,
	"description":"The Rob Roy Loop through Strathyre forest is a perfect cycling route for an active family. At just under 8 miles long it is perfect for a day's cycling among beautiful forests and lochs, with the chance to see Rob Roy's grave.",
	"categories": "Family",
	"image":"RobRoyLoop.jpg",
	"url": "https://www.lochlomond-trossachs.org/things-to-do/cycling/cycling-routes/rob-roy-loop/"
	},
	{
	"name": "Kelburn Castle near Largs, Ayrshire & Arran",
	"likes": 0,
	"description":"Kelburn Castle is a perfect family day out with plenty for kids (and adults) to do including pony trekking, an indoor playbarn, outdoor walks and a woodland adventure area.",
	"categories": "Family",
	"image":"KelburnCastle.jpg",
	"url": "https://www.kelburnestate.com"
	},
	{
	"name": "Sea Kayak Oban",
	"likes": 0,
	"description":"If you are looking for a nautical adventure then Oban Sea Kayak is the place for you! Head to Oban for wildlife, scenery and the chance to try out some amazing kayaking equipment with fully qualified instructors to guide you.",
	"categories": "Family",
	"image":"ObanKayak.jpg",
	"url": "https://www.seakayakoban.com"
	},
	{
	"name": "Monikie Country Park",
	"likes": 0,
	"description":"This is the place to be for a family day out in summer! Go on a woodland walk, spend some time birdwatching and then make use of the barbecue hire for an outdoor feast. Kids will enjoy the adventure play area too.",
	"categories": "Family",
	"image":"MonikiePark.jpg",
	"url": "http://archive.angus.gov.uk/leisureaa/rangerservice/monikie.htm"
	},
	{
	"name": "TRNSMT",
	"likes": 0,
	"description": "TRNSMT is Scotland's newest, most exciting festival. Returning in 2019 with a cracking line-up including George Ezra, Stormzy and Years & Years, this year's festival is not to be missed!",
	"categories": "Music",
	"image": "trnsmt.jpg",
	"url": "https://trnsmtfest.com/"
	},
	{
	"name": "King Tut's Wah Wah Hut",
	"likes": 0,
	"description":"King Tuts has been home to some of Glasgow's greatest gigs! Music lovers cannot miss out on a night here in Scotland's city of music.",
	"categories": "Music",
	"image":"king_tuts.jpg",
	"url": "https://www.kingtuts.co.uk/"
	},
	{
	"name": "Belladrum Tartan Heart Festival",
	"likes": 0,
	"description":"This year's Belladrum Tartan Heart Festival features an amazing line-up among some of the country's most breathtaking scenery.",
	"categories": "Music",
	"image":"belladrum.jpg",
	"url": "https://tartanheartfestival.co.uk/"
	},
	{
	"name": "The Islay Festival of Music and Malt",
	"likes": 0,
	"description":"Islay's Music and Malt festival is a celebration of all things Scottish. Come along and enjoy whisky tasting, Scottish folk music, Gaelic lessons and more.",
	"categories": "Music",
	"image":"islay_festival.jpg",
	"url": "https://www.islayfestival.com/"
	},
	{
	"name": "Summer Nights at The Bandstand",
	"likes": 0,
	"description":"Summer Nights returns to Kelvingrove Bandstand this year, with indie hits like Father John Misty and The National among the line up. This series of open-air concerts takes place throughout August in Glasgow's beautiful west end.",
	"categories": "Music",
	"image":"summer_nights.jpg",
	"url": "https://www.ticketmaster.co.uk/Summer-Nights-tickets/artist/1992315",
	},
	{
	"name": "Stramash Live Music Bar",
	"likes": 0,
	"description":"Stramash Live Music bar in Edinburgh is a vibrant place for music lovers, with jazz and folk performances among more contemporary gigs. It also offers live sport and a crowd-pleasing gastropub menu.",
	"categories": "Music",
	"image":"stramash.jpg",
	"url": "https://stramashedinburgh.com/"
	},
	{
	"name": "Burnsfest! 2019",
	"likes": 0,
	"description":"Burnsfest returns to Rozelle Park in Ayr in May 2019. This is a great family day out with food and craft stalls, poetry readings and live music from local bands.",
	"categories": "Music",
	"image":"burnsfest.jpg",
	"url": "http://www.burnsfestival.com/burnsfest/",
	},
	{
	"name": "The Barrowland Ballroom",
	"likes": 0,
	"description":"Arguably Glasgow's most iconic gig venue, any music fan should not pass up a night in the Barrowlands! No matter the band, there is always an electric atmosphere. Plus, the venue is easily accessible from Central Station.",
	"categories": "Music",
	"image":"barrowland_ballroom.jpg",
	"url": "http://barrowland-ballroom.co.uk/",
	},
	{
	"name": "Orkney Folk Festival",
	"likes": 0,
	"description":" Orkney Folk Festival is a traditional Scottish festival that exhibits classic folk and jazz performances. The festival is family friendly and also includes ceilidhs and dances.",
	"categories": "Music",
	"image":"orkney_folk_festival.jpg",
	"url": "https://www.orkneyfolkfestival.com/",
	},
	{
	"name": "Crofter’s Music Bar",
	"likes": 0,
	"description":"Crofters Music Bar in the popular town of Brodick on the Isle of Arran is a great place to go for good food and music. As a small, intimate venue, it allows you to really experience some of Scotland's best classic artists, while enjoying some delicious pub fayre!",
	"categories": "Music",
	"image":"crofters.jpg",
	"url": "https://croftersmusicbar.com/",
	},
	{
	"name": "The Gin to My Tonic Show",
	"likes": 0,
	"description":"Love gin? Then The Gin To My Tonic festival is the place you'll want to be going to.",
	"categories": "Food",
	"image":"gin_to_my_tonic.jpg",
	"url": "https://thegintomytonic.com/event/the-gin-to-my-tonic-show-glasgow-15th-17th-march-2019/"
	},
	{
	"name": "Scottish Vegan Festival",
	"likes": 0,
	"description":"The festival runs from 10:30 to 17:00. With the many number of food stalls, there will be a wide variety of vegan food to try! So, come along!",
	"categories": "Food",
	"image":"vegan_festival.jpg",
	"url": "https://www.vegfest.co.uk/event/scottish-vegan-festival-2/",
	},
	{
	"name": "Tennent’s Wellpark Brewery",
	"likes": 0,
	"description":"Fancy a Tennents pint? Want to learn more about your favourite beer? Why not go on the Tennants tour!",
	"categories": "Food",
	"image":"tennents_brewery.jpg",
	"url": "http://www.tennentstours.com/",
	},
	{
	"name": "Foodies’ Festival",
	"likes": 0,
	"description":"If you are a foodie then you will enjoy the Foodies' Festival!",
	"categories": "Food",
	"image":"foodies_festival.jpeg",
	"url": "http://foodiesfestival.com/",
	},
	{
	"name": "Spirit of Speyside Whisky Festival",
	"likes": 0,
	"description":"Not only will you be able to enjoy some whisky tasting but there will also be food, active outdoor events and music and performance for you to enjoy!",
	"categories": "Food",
	"image":"spirit_of_speyside.jpg",
	"url": "https://www.spiritofspeyside.com/"
	},
	{
	"name": "Tarbert Seafood Festival",
	"likes": 0,
	"description":"If you are a food lover and enjoy seafood, then this festival is where you would want to be!",
	"categories": "Food",
	"image":"tarbert_seafood_festival.jpg",
	"url": "http://www.tarbertfestivals.co.uk/festival-seafood.php",
	},
	{
	"name": "Penicuik Market",
	"likes": 0,
	"description":"A farmers market selling fresh grown fruit and vegetables. However, there are also stalls for jewellery, soaps and flowers!",
	"categories": "Food",
	"image":"penicuik_market.jpg",
	"url": "https://www.visitscotland.com/info/events/penicuik-market-p1598541"
	},
	{
	"name": "Autumn Fungi & Wild Food Foraging Walk",
	"likes": 0,
	"description":"Explore the autumn fungi and wild food with a 3 hour walk with Mark Williams of Galloway Wild Foods.",
	"categories": "Food",
	"image":"autumn_fungi_walk.jpg",
	"url": "http://www.gallowaywildfoods.com/product/autumn_fungi_wild_food_foraging_walk_dumfries/"
	},
	{
	"name": "Highland Haggis Festival",
	"likes": 0,
	"description":"Come along to Highland Haggis Festival to try out true authentic Scottish haggis.",
	"categories": "Food",
	"image":"highland_haggis_festival.jpg",
	"url": "https://www.highlandhaggisfest.co.uk/",
	},
	{
	"name": "Highland Food & Drink Festival",
	"likes": 0,
	"description":"Over 50 exhibitors and many different foods to try!",
	"categories": "Food",
	"image":"highland_food_and_drink_festival.png",
	"url": "https://www.eventbrite.co.uk/e/highland-food-drink-festival-tickets-53133201837"
	}		
	]

	for c in Category.objects.all():
		for e in Event.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(e)))

	for item in adverts:
		a = add_ad(item["advertText"], item["email"])
		print(format(str(a)))

	for item in categories:
		f = add_categories(item["name"])
		print(format(str(f)))


	for item in events:
		e = add_events(item["name"], item["likes"], item["description"], get_categories(item["categories"]), item["image"], item["url"])
		print(format(str(e)))

def add_ad(advertText, email):
	a = Advert.objects.get_or_create(advertText=advertText, email=email)
	return a


def add_categories(name):
	f = Categories.objects.get_or_create(name = name)
	return f

def get_categories(name):
	categories = Categories.objects.get(name = name)
	return categories


def add_events(name, likes, description, categories, image, url):
	r = Events.objects.get_or_create(name = name, likes=likes, description = description, categories = categories, image = image, url=url)
	return r


if __name__ == '__main__':
	print("Starting Whisk You Away population script...")
	populate()