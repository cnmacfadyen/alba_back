from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from whiskyouaway.models import Category, Event, UserProfile, Review, Advert, Categories, Events
from whiskyouaway.forms import UserForm, UserProfileForm, Review, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from datetime import datetime


# Create your views here.

def index(request):
	events_list = Events.objects.order_by('-likes')[:5]
	# category_list = Categories.objects.order_by('name')
	context_dict = {'eventsList': events_list}

	response = render(request, 'whiskyouaway/home.html', context=context_dict)

	return response
	# response = render(request, 'whiskyouaway/home.html', {})
	# return response

def about(request):
	return render(request, 'whiskyouaway/about.html', {})

def categories(request):
	return render(request, 'whiskyouaway/categories.html', {})

def contact_us(request):
	return render(request, 'whiskyouaway/contact_us.html', {})

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
	# context_dict= {}

	# return render(request, 'whiskyouaway/event.html', context_dict)

	try:
		event = Events.objects.get(slug=events_name_slug)
	except Events.DoesNotExist:
		return redirect('index')

	return render(request, 'whiskyouaway/event.html', {'event': event})


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
	
#def register(request):
#	return render(request, 'whiskyouaway/register.html', {})

#def user_login(request):
#	return render(request, 'whiskyouaway/login.html', {})

def restricted(request):
	return render(request, 'whiskyouaway/restricted.html', {})

#def user_logout(request):
#	return render(request, 'whiskyouaway/logout.html', {})

def meet_up(request):
	advert_list = Advert.objects.order_by('email')
	context_dict = {'advertList': advert_list}
	return render(request, 'whiskyouaway/meet_up.html', context=context_dict)

def view_attractions(request):
	return render(request, 'whiskyouaway/view_attractions.html', {})

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

#def register(request):
#	registered = False
#	if request.method == 'POST':
#		user_form = UserForm(data=request.POST)
#		profile_form = UserProfileForm(data=request.POST)
#
#		if user_form.is_valid() and profile_form.is_valid():
#			user = user_form.save()
#			user.set_password(user.password)
#			user.save()
#			profile = profile_form.save(commit=False)
#			profile.user = user
#
#			if 'picture' in request.FILES:
#				profile.picture = request.FILES['picture']
#			profile.save()
#			registered = True
#		else:
#			print(user_form.errors, profile_form.errors)
#	else:
#		user_form = UserForm()
#		profile_form = UserProfileForm()
#
#	return render(request, 'whiskyouaway/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

#def user_login(request):
#	if request.method == 'POST':
#		username = request.POST.get('username')
#		password = request.POST.get('password')
#		user = authenticate(username=username, password=password)
#		if user:
#			if user.is_active:
#				login(request, user)
#				return HttpResponseRedirect(reverse('index'))
#			else:
#				return HttpResponse("Your account is disabled.")
#		else:
#			print("Invalid login details: {0}, {1}".format(username, password))
#			return HttpResponse("Invalid login details supplied.")

#	else:
#		return render(request, 'whiskyouaway/login.html', {})

#@login_required
#def user_logout(request):
#	logout(request)
#	return HttpResponseRedirect(reverse('index'))