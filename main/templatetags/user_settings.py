from django import template
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def user_school_header(user):
    username = user.username
    if not username:
        username = 'Guest'

    return format_html(f'<h2 class="text text-justify my-2 display-4">'
                       f'Welcome {username}</h2>')
