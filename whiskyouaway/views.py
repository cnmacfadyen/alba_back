from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from whiskyouaway.models import Category, Page, UserProfile
# from whiskyouaway.forms import CategoryForm, PageForm, UserForm, UserProfileForm
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
