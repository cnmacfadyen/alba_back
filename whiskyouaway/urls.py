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
	url(r'^events/(?P<events_name_slug>[\w\-]+)/review/$', views.reviews, name='reviews'),
	url(r'^like/$', views.like_event, name='like_event'),
	url(r'^interests_map/', views.interests_map, name='interests_map'),
	url(r'^register_profile/$', views.register_profile, name='register_profile'),
	url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
	url(r'^profiles/$', views.list_profiles, name='list_profiles'),
	url(r'^restricted/', views.restricted, name='restricted'),
	url(r'^adverts/', views.adverts, name='adverts'),
	url(r'^contact_us/$', views.contact_us, name='contact_us'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^meet_up/$', views.meet_up, name='meet_up'),
	url(r'^events/$', views.events, name='events'),
	
	# uses slug to get individual pages for events
	url(r'^events/(?P<events_name_slug>[\w\-]+)/$',
		views.show_events,
		name='show_events'),


]