from django.contrib import admin
from whiskyouaway.models import UserProfile, Categories, Events, Review, Advert, UserCategories





class AdvertAdmin(admin.ModelAdmin):
	list_display = ('advertText', 'email')

class ReviewAdmin(admin.ModelAdmin):
	list_display = ('review', 'event')

# class UserProfile(admin.ModelAdmin):
# 	list_display=('username', 'website')

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Categories)
admin.site.register(Events)
admin.site.register(Review)
admin.site.register(Advert, AdvertAdmin)
admin.site.register(UserCategories)