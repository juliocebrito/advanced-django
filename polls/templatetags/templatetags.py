from django import template
import calendar

register = template.Library()


@register.filter
def weekday(value):
    today = int(value)
    return calendar.day_name[today]