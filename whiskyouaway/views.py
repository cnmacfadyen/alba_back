from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from whiskyouaway.models import UserProfile, Review, Advert, Categories, Events
from whiskyouaway.forms import UserForm, UserProfileForm, Review, CommentForm, ContactForm, AdvertForm
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
	events_list = Events.objects.order_by('-likes')[:5]
	category_list = Categories.objects.order_by('name')
	context_dict = {'eventsList': events_list,
					'categoryList': category_list}

	response = render(request, 'whiskyouaway/home.html', context=context_dict)
	return response

def about(request):
	return render(request, 'whiskyouaway/about.html', {})

def categories(request):
	return render(request, 'whiskyouaway/categories.html', {})

def profile(request):
	return render(request, 'whiskyouaway/profile.html', {})

@login_required
def adverts(request):
	form = AdvertForm()

	# A HTTP POST?
	if request.method == 'POST':
		form = AdvertForm(request.POST)

		# Have we been provided with a valid form?
		if form.is_valid():
			# save the new advert to the database
			ad = form.save(commit=True)
			# redirect to the meet up page
			return meet_up(request)
		else:
			#print errors to the terminal
			print(form.errors)

	# will handle the bad form, new form, or no form supplied cases
	# render the form with error messages (if any)
	return render(request, 'whiskyouaway/adverts.html', {'form': form})

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
		form = CommentForm()

		context_dict['reviews'] = reviews

		if request.method == 'POST':

			form.events = events
			form = CommentForm(request.POST)

			if form.is_valid():
				getInfo = form.save(commit=False)
				getInfo.events=Events.objects.get(slug=events_name_slug)
				getInfo.user = request.user
		
				getInfo.save()

				info_dict = {"comment": getInfo.comment, "user": request.user.username,"date": getInfo.date_posted.strftime('%B %d, %Y, %I:%M %p')}
				return HttpResponse(json.dumps(info_dict), content_type="application/json")

			else:
				print(form.errors)

	except Events.DoesNotExist:

		context_dict['events'] = None
		context_dict['reviews'] = None

	context_dict = {'form': form, 'events': events, 'reviews':reviews}
	return render(request, 'whiskyouaway/event.html', context_dict)


def like_event(request):
    event_id = None
    if request.method == 'GET':
        event_id = request.GET['event_id']
    likes = 0
    if event_id:
        event = Events.objects.get(id=int(event_id))
        if event:
            likes = event.likes + 1
            event.likes = likes
            event.save()
    return HttpResponse(likes)


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

