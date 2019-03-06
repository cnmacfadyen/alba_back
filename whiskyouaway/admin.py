from django.contrib import admin
from whiskyouaway.models import Category, Event, CategoryContainer,UserProfile, Review


# Register your models here.
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(CategoryContainer)
admin.site.register(UserProfile)
admin.site.register(Review)