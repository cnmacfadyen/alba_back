from django import template
from whiskyouaway.models import Category

register = template.Library()

@register.inclusion_tag('whiskyouaway/cats.html')

def get_category_list(cat=None):
	return{'cats': Category.objects.all(),
			'act_cat': cat}