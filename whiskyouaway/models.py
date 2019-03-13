from django.db import models
from django.template.defaultfilters  import slugify
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

		
class Event(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()

	def __str__(self):
		return self.title

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	def __str__(self):
		return self.user.username

class Review(models.Model):
	events = models.ForeignKey(Event)
	writtenReview = models.CharField(max_length=200)
	username = models.CharField(max_length=50)
	rating = models.IntegerField()

class Advert(models.Model):
	# category = models.ForeignKey(Category)
	advertText = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	# user = models.OneToOneField(User)
	def __str__(self):
		return self.email

class ContactUs(models.Model):
	firstname = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	question = models.CharField(max_length=200)



