from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)

	# def save(self, *args, **kwargs):
	# 	self.slug = slugify(self.name)
	# 	super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

class CategoryContainer(models.Model):
	category_name = models.CharField(max_length=128, unique=True)

	def __str__(self):
		return self.category_name

class Event(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()

	def __str__(self):
		return self.title

