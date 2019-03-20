from django.db import models
from django import forms
from django.template.defaultfilters  import slugify
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


# Create your models here.
class Categories(models.Model):
	name = models.CharField(max_length=128, unique=True) #name has to be unique
	image = models.ImageField(upload_to='static/categories_images', blank=False)

	def __str__(self):
		return self.name
		
class Events(models.Model):
	
	user = models.CharField(max_length=128)
	def __unicode__(self):
		return self.name
	# All of these fields will be needed when creating the population script
	name = models.CharField(max_length=128, null=True)
	likes = models.IntegerField(default=0)
	description = models.CharField(max_length=9999, null=True)
	categories = models.ForeignKey(Categories)
	slug = models.SlugField(null=True, blank=True)
	image = models.ImageField(upload_to='events_images', blank=False)
	url = models.URLField(max_length=128)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Events, self).save(*args, **kwargs)

	# returns name
	def __str__(self):
		return self.name


class Review(models.Model):
	events = models.ForeignKey(Events)
	user = models.CharField(max_length=128)
	def __unicode__(self):
		return self.name
	comment = models.CharField(max_length=2000, null=True)
	date_posted = models.DateTimeField(auto_now=True)

	# returns comment
	def __str__(self):
		return self.comment


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	def __str__(self):
		return self.user.username

# Set the fields to false so that it doesn't matter whether an image/website is uploaded or not
class UserProfileForm(forms.ModelForm):
	website = forms.URLField(required=False)
	picture = forms.ImageField(required=False)

	class Meta:
		model = UserProfile
		exclude = ('user',)


class Advert(models.Model):
	advertText = models.CharField(max_length=2000)
	email = models.CharField(max_length=200)
	def __str__(self):
		return self.email

class ContactUs(models.Model):
	firstname = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	question = models.CharField(max_length=200)

# Hoping to connect this up with user later 
class UserCategories(models.Model):
	CATEGORY_CHOICES = (
		('Music', 'Music'),
		('Animals', "Animals"),
		('Nightlife', 'Nightlife'),
		('Sport', 'Sport'),
		('Outdoors', 'Outdoors'),
		('History', 'History'),
		('Family', 'Family'),
		('Food', 'Food')
		)
	title = MultiSelectField(choices=CATEGORY_CHOICES)






