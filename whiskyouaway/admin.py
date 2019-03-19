from django.contrib import admin
from whiskyouaway.models import Category, Event, UserProfile, Categories, Events, Review, Advert, UserCategories



class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

class AdvertAdmin(admin.ModelAdmin):
	list_display = ('advertText', 'email')

class ReviewAdmin(admin.ModelAdmin):
	list_display = ('review', 'event')

# class UserProfile(admin.ModelAdmin):
# 	list_display=('username', 'website')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(UserProfile)
admin.site.register(Categories)
admin.site.register(Events)
admin.site.register(Review)
admin.site.register(Advert, AdvertAdmin)
admin.site.register(UserCategories)