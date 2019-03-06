from django import forms
from django.contrib.auth.models import User
from whiskyouaway.models import Category,  UserProfile, Review

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture')

class ReviewForm(forms.ModelForm):
	class meta:
		model = Review
		fields = ('username', 'review', 'ratings')