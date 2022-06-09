from django.contrib.auth.models import User

from django import template

register = template.Library()


def author_details(value):
    """  """
    if not is instance(value, User):
      return ""

    if value.first_name != "" or value.last_name != "":
      return value.first_name +  " " + value.last_name
    
    return value.username



register.filter('author_details', author_details)
