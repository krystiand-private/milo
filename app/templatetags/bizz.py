import datetime

from django import template

from app.models import User

register = template.Library()


def calc_bizz(num):
    return ("Bizz" if (num % 3) == 0 else "") + ("Fuzz" if (num % 5) == 0 else "")


@register.simple_tag
def bizz(num):
    return calc_bizz(num)
