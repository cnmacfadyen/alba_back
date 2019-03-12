from django.contrib import admin
from whiskyouaway.models import Category, Event, CategoryContainer, UserProfile, Review


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

# class UserProfile(admin.ModelAdmin):
# 	prepopulated_fields=('username')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(CategoryContainer)
admin.site.register(UserProfile)
admin.site.register(Review)