from django import forms
from django.contrib.auth.models import User
from whiskyouaway.models import Category, UserProfile, Review, ContactUs, Advert

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('user',)

class ReviewForm(forms.ModelForm):
	class meta:
		model = Review
		fields = ('username', 'review', 'ratings')

class AdvertForm(forms.ModelForm):
	class meta:
		model = Advert
		fields = ('event', 'advertText', 'user')

class ContactUs(forms.ModelForm):
	class meta:
		model = ContactUs
		fields = ('firstname', 'surname', 'email', 'issue', 'question')