import datetime

from django import template

from app.models import User

register = template.Library()


def check_perms(user: User):
    if isinstance(user, User):
        date_of_birth = user.date_of_birth or datetime.date.max
        return "allowed" if datetime.date.today() - date_of_birth >= datetime.timedelta(days=13 * 365) else "blocked"

    return "blocked"


@register.simple_tag(takes_context=True)
def perms(context, user=None):
    request = context['request']
    return check_perms(user or request.user)
