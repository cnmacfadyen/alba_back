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

	# adds the inputs to the Review model
	class Meta:
		model = Review
		fields = ('comment', )
	
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('user',)

class AdvertForm(forms.ModelForm):
	class meta:
		model = Advert
		fields = ('event', 'advertText', 'email', 'user')

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)





