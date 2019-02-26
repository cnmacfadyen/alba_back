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
	context_dict = {'boldmessage': "Whisk You Away test!"}
	response = render(request, 'whiskyouaway/home.html', context=context_dict)
	return response