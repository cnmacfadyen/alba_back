from django.contrib import admin
from whiskyouaway.models import Category, Event, UserProfile, Categories, Events, Review, Advert


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

class AdvertAdmin(admin.ModelAdmin):
	list_display = ('advertText', 'email')

# class UserProfile(admin.ModelAdmin):
# 	prepopulated_fields=('username')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(UserProfile)
admin.site.register(Categories)
admin.site.register(Events)
admin.site.register(Review)
admin.site.register(Advert, AdvertAdmin)