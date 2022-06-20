from django.contrib.auth.models import User
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django import template

register = template.Library()


def author_details(author, current_user):
    # """  """
    # if not isinstance(value, User):
    #   return ""

    # if value.first_name != "" or value.last_name != "":
    #   if value.email:
    #     email = escape(value.email)
    #     # return f'<a href="mailto:{email}">'
    #     prefix = format_html('<a href="mailto:{}">', email)
    #     return prefix
    #   return value.first_name +  " " + value.last_name
    
    # if value.email:
    #     email = escape(value.email)
    #     # return f'<a href="mailto:{email}">'
    #     prefix = format_html('<a href="mailto:{}">', email)
    #     return prefix

    print("current_user---",current_user)
    if not isinstance(author, User):
        # return empty string as safe default
        return ""

    if author == current_user:
      return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)
        



register.filter('author_details', author_details)
