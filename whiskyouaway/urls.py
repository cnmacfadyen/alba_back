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
	# url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
	# url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
	url(r'^categories/(?P<category_name_slug>[\w\-]+)/reviews/$', views.reviews, name='reviews'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^restricted/', views.restricted, name='restricted'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^contact_us/$', views.contact_us, name='contact_us'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^meet_up/$', views.meet_up, name='meet_up'),
	url(r'^view_attractions/$', views.view_attractions, name='view_attractions'),

]