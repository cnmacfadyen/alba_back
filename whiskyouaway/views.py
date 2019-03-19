from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from whiskyouaway.models import Category, Event, UserProfile, Review, Advert, Categories, Events
from whiskyouaway.forms import UserForm, UserProfileForm, Review, CommentForm, ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from datetime import datetime
from django.core.mail import send_mail
from datetime import datetime
import json
from django.db.models import Q
from django.db.models import Avg

# Create your views here.
def contact_us(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			
			subject = form.cleaned_data['subject']
			email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']

			send_mail(subject+" - " + email, message, email, ['whiskyouaway11@gmail.com'])
			return redirect('index')
	return render(request, "whiskyouaway/contact_us.html", {'form': form})

def successView(request):
	return HttpResponse('Success! Thank you for your message.')

def index(request):
	events_list = Events.objects.order_by('name')[:5]
	category_list = Categories.objects.order_by('name')
	context_dict = {'eventsList': events_list,
					'categoryList': category_list}

	response = render(request, 'whiskyouaway/home.html', context=context_dict)

	return response
	# response = render(request, 'whiskyouaway/home.html', {})
	# return response

def about(request):
	return render(request, 'whiskyouaway/about.html', {})

def categories(request):
	return render(request, 'whiskyouaway/categories.html', {})

# def contact_us(request):
# 	return render(request, 'whiskyouaway/contact_us.html', {})

def profile(request):
	return render(request, 'whiskyouaway/profile.html', {})

@login_required
def adverts(request):
	return render(request, 'whiskyouaway/adverts.html', {})

def interests_map(request):
	return render(request, 'whiskyouaway/interests_map.html', {})

def events(request):
	events_list = Events.objects.order_by('name')

	category_list = Categories.objects.order_by('name')
	context_dict = {'eventsList': events_list,
					'categoryList': category_list}

	response = render(request, 'whiskyouaway/events.html', context=context_dict)

	return response

def show_events(request, events_name_slug, *args, **kwargs):
	context_dict= {}

	try:
		events = Events.objects.get(slug=events_name_slug)
		reviews = Review.objects.filter(events=events).order_by('-date_posted')
		scoreAvg = Review.objects.filter(events=events).aggregate(Avg('rating'))['rating__avg']
		form = CommentForm()

		context_dict['reviews'] = reviews

		if request.method == 'POST':

			form.events = events
			form = CommentForm(request.POST)

			if form.is_valid():
				a = form.save(commit=False)
				a.events=Events.objects.get(slug=events_name_slug)
		
				a.save()

				info_dict = {"comment": a.comment, "date": a.date_posted.strftime('%B %d, %Y, %I:%M %p')}
				return HttpResponse(json.dumps(info_dict), content_type="application/json")

			else:
				print(form.errors)

	except Events.DoesNotExist:

		context_dict['events'] = None
		context_dict['reviews'] = None

	context_dict = {'form': form, 'events': events, 'reviews':reviews}
	return render(request, 'whiskyouaway/event.html', context_dict)


@login_required 
def register_profile(request): 
	form = UserProfileForm()
	if request.method == 'POST': 
		form = UserProfileForm(request.POST, request.FILES) 
		if form.is_valid(): 
			user_profile = form.save(commit=False) 
			user_profile.user = request.user 
			user_profile.save()
			
			return redirect('index') 
		else: 
			print(form.errors)

	context_dict = {'form':form}

	return render(request, 'whiskyouaway/profile_registration.html', context_dict)

@login_required
def profile(request, username):
	try:
		user = User.objects.get(username=username)
	except User.DoesNotExist:
		return redirect('index')

	userprofile = UserProfile.objects.get_or_create(user=user)[0]
	form = UserProfileForm({'website': userprofile.website, 'picture': userprofile})

	if request.method == 'POST':
		form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
		if form.is_valid():
			form.save(commit=True)
			return redirect('profile', user.username)
		else:
			print(form.errors)
	return render(request, 'whiskyouaway/profile.html', {'userprofile': userprofile, 'selecteduser': user, 'form': form})


@login_required
def list_profiles(request):
	userprofile_list = UserProfile.objects.all()

	return render(request, 'whiskyouaway/list_profiles.html',
		{'userprofile_list': userprofile_list})


def restricted(request):
	return render(request, 'whiskyouaway/restricted.html', {})

def meet_up(request):
	advert_list = Advert.objects.order_by('email')
	context_dict = {'advertList': advert_list}
	return render(request, 'whiskyouaway/meet_up.html', context=context_dict)

@login_required
def reviews(request, events_name_slug, *args, **kwargs):
	try:
		event = Events.objects.get(slug=events_name_slug)
	except Events.DoesNotExist:
		return redirect('index')

	return render(request, 'whiskyouaway/review.html', {})

def get_category_list(cat=None):
	return {'cats': Category.objects.all(), 'act_cat': cat}

def show_category(request, category_name_slug):	
	context_dict = {}

	try:
		category = Category.objects.get(slug=category_name_slug)
		events = Event.objects.filter(category=category)
		context_dict['events'] = events
		context_dict['category'] = category
	except Category.DoesNotExist:
		context_dict['category'] = None
		context_dict['events'] = None
	return render(request, 'whiskyouaway/categories.html', context_dict)