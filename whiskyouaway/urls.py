from django.conf.urls import url
from whiskyouaway import views
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^categories/$', views.categories, name='categories'),
	url(r'^categories/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
	url(r'^categories/(?P<category_name_slug>[\w\-]+)/reviews/$', views.reviews, name='reviews'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^restricted/', views.restricted, name='restricted'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^contact_us/$', views.contact_us, name='contact_us'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^meet_up/$', views.meet_up, name='meet_up'),
	url(r'^view_attractions/$', views.view_attractions, name='view_attractions'),
	# animal urls
	url(r'^categories/animals/dog_jog/$', views.dog_jog, name='dog_jog'),
	url(r'^categories/animals/dog_lover/$', views.dog_lover, name='dog_lover'),
	url(r'^categories/animals/edinburgh_dogs/$', views.edinburgh_dogs, name='edinburgh_dogs'),
	url(r'^categories/animals/edinburgh_zoo/$', views.edinburgh_zoo, name='edinburgh_zoo'),
	url(r'^categories/animals/deep_sea_world/$', views.deep_sea_world, name='deep_sea_world'),
	url(r'^categories/animals/blair_drummond/$', views.blair_drummond, name='blair_drummond'),
	url(r'^categories/animals/highland_wildlife/$', views.highland_wildlife, name='highland_wildlife'),
	url(r'^categories/animals/chihuahua_cafe/$', views.chihuahua_cafe, name='chihuahua_cafe'),
	url(r'^categories/animals/cat_cafe/$', views.cat_cafe, name='cat_cafe'),
	# nightlife urls
	url(r'^categories/nightlife/blue_dog/$', views.blue_dog, name='blue_dog'),
	url(r'^categories/nightlife/tingle/$', views.tingle, name='tingle'),
	url(r'^categories/nightlife/firewater/$', views.firewater, name='firewater'),
	url(r'^categories/nightlife/cathouse/$', views.cathouse, name='cathouse'),
	url(r'^categories/nightlife/frankenstein/$', views.frankenstein, name='frankenstein'),
	url(r'^categories/nightlife/hive/$', views.hive, name='hive'),
	# sport urls
	url(r'^categories/sport/indoor_athletics/$', views.indoor_athletics, name='indoor_athletics'),
	url(r'^categories/sport/pro14_final/$', views.pro14_final, name='pro14_final'),
	url(r'^categories/sport/horse_trials/$', views.horse_trials, name='horse_trials'),
	url(r'^categories/sport/solheim_cup/$', views.solheim_cup, name='solheim_cup'),
	url(r'^categories/sport/spfl/$', views.spfl, name='spfl'),
	url(r'^categories/sport/water_ski/$', views.water_ski, name='water_ski'),
	url(r'^categories/sport/boat_show/$', views.boat_show, name='boat_show'),
	url(r'^categories/sport/british_swimming/$', views.british_swimming, name='british_swimming'),
	url(r'^categories/sport/darts/$', views.darts, name='darts'),
	url(r'^categories/sport/cycling_world_cup/$', views.cycling_world_cup, name='cycling_world_cup'),
	# outdoor urls
	url(r'^categories/outdoors/tattoo/$', views.tattoo, name='tattoo'),
	url(r'^categories/outdoors/glasglow/$', views.glasglow, name='glasglow'),
	url(r'^categories/outdoors/highland_games/$', views.highland_games, name='highland_games'),
	url(r'^categories/outdoors/fire_festival/$', views.fire_festival, name='fire_festival'),
	url(r'^categories/outdoors/nature_festival/$', views.nature_festival, name='nature_festival'),
	url(r'^categories/outdoors/bard_botanics/$', views.bard_botanics, name='bard_botanics'),
	url(r'^categories/outdoors/outdoor_survival/$', views.outdoor_survival, name='outdoor_survival'),
	url(r'^categories/outdoors/west_highland_way/$', views.west_highland_way, name='west_highland_way'),
	url(r'^categories/outdoors/quadmania/$', views.quadmania, name='quadmania'),
	url(r'^categories/outdoors/outdoor_explore/$', views.outdoor_explore, name='outdoor_explore'),
	# history urls
	url(r'^categories/history/InveraryCastle/$', views.inverary, name='inverary'),
	url(r'^categories/history/DunrobinCastle/$', views.dunrobin, name='dunrobin'),
	url(r'^categories/history/EdinburghCastle/$', views.edinburgh, name='edinburgh'),
	url(r'^categories/history/StirlingCastle/$', views.stirling, name='stirling'),
	url(r'^categories/history/EileanDonanCastle/$', views.eilean, name='eilean'),
	url(r'^categories/history/KilchurnCastle/$', views.kilchurn, name='kilchurn'),
	url(r'^categories/history/WritersMuseum/$', views.writers, name='writers'),
	url(r'^categories/history/KelvingroveMuseum/$', views.kelvingrove, name='kelvingrove'),
	url(r'^categories/history/NationalMuseums/$', views.national_museums, name='national_museums'),
	url(r'^categories/history/VADundee/$', views.vadundee, name='vadundee'),
	url(r'^categories/history/RiversideMuseum/$', views.riverside, name='riverside'),
	# family urls
	url(r'^categories/family/SpeysideWay/$', views.speyside, name='speyside'),
	url(r'^categories/family/RobRoyLoop/$', views.robroy, name='robroy'),
	url(r'^categories/family/KelburnCastle/$', views.kelburn, name='kelburn'),
	url(r'^categories/family/ObanKayak/$', views.kayak, name='kayak'),
	url(r'^categories/family/MonikiePark/$', views.monikie, name='monikie'),


]