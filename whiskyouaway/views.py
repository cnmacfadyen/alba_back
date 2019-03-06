from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from whiskyouaway.models import Category, Event, UserProfile, Review
from whiskyouaway.forms import UserForm, UserProfileForm, Review
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from datetime import datetime


# Create your views here.

def index(request):
	response = render(request, 'whiskyouaway/home.html', {})
	return response

def about(request):
	return render(request, 'whiskyouaway/about.html', {})

def categories(request):
	return render(request, 'whiskyouaway/categories.html', {})

def contact_us(request):
	return render(request, 'whiskyouaway/contact_us.html', {})

def profile(request):
	return render(request, 'whiskyouaway/profile.html', {})

#def register(request):
#	return render(request, 'whiskyouaway/register.html', {})

#def user_login(request):
#	return render(request, 'whiskyouaway/login.html', {})

def restricted(request):
	return render(request, 'whiskyouaway/restricted.html', {})

#def user_logout(request):
#	return render(request, 'whiskyouaway/logout.html', {})

def meet_up(request):
	return render(request, 'whiskyouaway/meet_up.html', {})

def view_attractions(request):
	return render(request, 'whiskyouaway/view_attractions.html', {})

@login_required
def reviews(request):
	return render(request, 'whiskyouaway/reviews.html', {})

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

def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'whiskyouaway/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")

	else:
		return render(request, 'whiskyouaway/login.html', {})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

# animal pages

def dog_jog(request):
	return render(request, 'whiskyouaway/dog_jog.html', {})

def dog_lover(request):
	return render(request, 'whiskyouaway/dog_lover.html', {})

def edinburgh_dogs(request):
	return render(request, 'whiskyouaway/edinburgh_dogs.html', {})

def edinburgh_zoo(request):
	return render(request, 'whiskyouaway/edinburgh_zoo.html', {})

def deep_sea_world(request):
	return render(request, 'whiskyouaway/deep_sea_world.html', {})

def blair_drummond(request):
	return render(request, 'whiskyouaway/blair_drummond.html', {})

def highland_wildlife(request):
	return render(request, 'whiskyouaway/highland_wildlife.html', {})

def chihuahua_cafe(request):
	return render(request, 'whiskyouaway/chihuahua_cafe.html', {})

def cat_cafe(request):
	return render(request, 'whiskyouaway/cat_cafe.html', {})

# nightlife pages

def blue_dog(request):
	return render(request, 'whiskyouaway/blue_dog.html', {})

def tingle(request):
	return render(request, 'whiskyouaway/tingle.html', {})

def firewater(request):
	return render(request, 'whiskyouaway/firewater.html', {})

def cathouse(request):
	return render(request, 'whiskyouaway/cathouse.html', {})

def frankenstein(request):
	return render(request, 'whiskyouaway/frankenstein.html', {})

def hive(request):
	return render(request, 'whiskyouaway/hive.html', {})


# sport pages

def indoor_athletics(request):
	return render(request, 'whiskyouaway/indoor_athetics.html', {})

def pro14_final(request):
	return render(request, 'whiskyouaway/pro14_final.html', {})

def horse_trials(request):
	return render(request, 'whiskyouaway/horse_trials.html', {})

def solheim_cup(request):
	return render(request, 'whiskyouaway/solheim_cup.html', {})

def spfl(request):
	return render(request, 'whiskyouaway/spfl.html', {})

def water_ski(request):
	return render(request, 'whiskyouaway/water_ski.html', {})

def boat_show(request):
	return render(request, 'whiskyouaway/boat_show.html', {})

def british_swimming(request):
	return render(request, 'whiskyouaway/british_swimming.html', {})

def darts(request):
	return render(request, 'whiskyouaway/darts.html', {})

def cycling_world_cup(request):
	return render(request, 'whiskyouaway/cycling_world_cup.html', {})

# outdoor pages

def tattoo(request):
	return render(request, 'whiskyouaway/tattoo.html', {})

def glasglow(request):
	return render(request, 'whiskyouaway/glasglow.html', {})

def highland_games(request):
	return render(request, 'whiskyouaway/highland_games.html', {})

def fire_festival(request):
	return render(request, 'whiskyouaway/fire_festival.html', {})

def nature_festival(request):
	return render(request, 'whiskyouaway/nature_festival.html', {})

def bard_botanics(request):
	return render(request, 'whiskyouaway/bard_botanics.html', {})

def outdoor_survival(request):
	return render(request, 'whiskyouaway/outdoor_survival.html', {})

def west_highland_way(request):
	return render(request, 'whiskyouaway/west_highland_way.html', {})

def quadmania(request):
	return render(request, 'whiskyouaway/quadmania.html', {})

def outdoor_explore(request):
	return render(request, 'whiskyouaway/outdoor_explore.html', {})

# history pages

def inverary(request):
	return render(request, 'whiskyouaway/InveraryCastle.html', {})

def dunrobin(request):
	return render(request, 'whiskyouaway/DunrobinCastle.html', {})

def edinburgh(request):
	return render(request, 'whiskyouaway/EdinburghCastle.html', {})

def stirling(request):
	return render(request, 'whiskyouaway/StirlingCastle.html', {})

def eilean(request):
	return render(request, 'whiskyouaway/EileanDonanCastle.html', {})

def kilchurn(request):
	return render(request, 'whiskyouaway/KilchurnCastle.html', {})

def writers(request):
	return render(request, 'whiskyouaway/WritersMuseum.html', {})

def kelvingrove(request):
	return render(request, 'whiskyouaway/kelvingroveMuseum.html', {})

def national_museums(request):
	return render(request, 'whiskyouaway/NationalMuseums.html', {})

def vadundee(request):
	return render(request, 'whiskyouaway/VADundee.html', {})

def riverside(request):
	return render(request, 'whiskyouaway/RiversideMuseum.html', {})

# family pages

def speyside(request):
	return render(request, 'whiskyouaway/SpeysideWay.html', {})

def robroy(request):
	return render(request, 'whiskyouaway/RobRoyLoop.html', {})

def kelburn(request):
	return render(request, 'whiskyouaway/KelburnCastle.html', {})

def kayak(request):
	return render(request, 'whiskyouaway/ObanKayak.html', {})

def monikie(request):
	return render(request, 'whiskyouaway/MonikiePark.html', {})

# music pages

# food pages
	
