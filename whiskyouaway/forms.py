from django import forms
from django.contrib.auth.models import User
from whiskyouaway.models import Category, UserProfile, Review, ContactUs, Advert, Categories, Events

class CommentForm(forms.ModelForm):

	# Gets the user who is posting the comment
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(CommentForm, self).__init__(*args, **kwargs)

	# fields for a comment
	comment = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'cols': 60, 'rows': 3}))
	rating = forms.IntegerField(help_text="Rate this Event", min_value=1, max_value=5)

	# adds the inputs to the Review model
	class Meta:
		model = Review
		fields = ('comment', 'rating')
		exclude = ('user', 'recipe')
	
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
		fields = ('event', 'advertText', 'email', 'user')

class ContactUs(forms.ModelForm):
	class meta:
		model = ContactUs
		fields = ('firstname', 'surname', 'email', 'issue', 'question')