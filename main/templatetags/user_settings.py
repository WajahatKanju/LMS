from django import template
from main.models import Settings
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def user_school_header(user):
    username = user.username
    if not username:
        username = 'Guest'
    try:
        setting = Settings.objects.get(employee__user_id__exact=user.id)
        selected_school = setting.selected_school
    except Settings.DoesNotExist:
        selected_school = 'No School Selected'

    return format_html(f'<h2 class="text text-justify my-2 display-4">' \
           f'Welcome {username } To { selected_school }</h2>')
