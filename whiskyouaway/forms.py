from django import forms
from django.contrib.auth.models import User
from whiskyouaway.models import UserProfile, Review, ContactUs, Advert, Categories, Events

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
		fields = ('picture','website')

class AdvertForm(forms.ModelForm):
	email = forms.EmailField(help_text="Email:",required=True)
	advertText = forms.CharField(help_text="Message:",widget=forms.Textarea, required=True)

	class Meta:
		model = Advert
		fields = ('advertText', 'email')

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)






