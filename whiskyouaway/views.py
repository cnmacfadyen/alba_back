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
	context_dict = {}
	response = render(request, 'whiskyouaway/contact_us.html', context_dict)
	return render

def profile(request):
	return render(request, 'whiskyouaway/profile.html', {})

def register(request):
	return render(request, 'whiskyouaway/register.html', {})

def user_login(request):
	return render(request, 'whiskyouaway/login.html', {})

def restricted(request):
	return render(request, 'whiskyouaway/restricted.html', {})

def user_logout(request):
	return render(request, 'whiskyouaway/logout.html', {})

def meet_up(request):
	return render(request, 'whiskyouaway/meet_up.html', {})

def view_attractions(request):
	return render(request, 'whiskyouaway/view_attractions.html', {})
