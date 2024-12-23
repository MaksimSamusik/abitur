from django import template
from django.contrib.auth.models import User
from django.utils import timezone

from entrants.models import *

register = template.Library()


@register.simple_tag()
def get_posts():
    return Services.objects.all()

