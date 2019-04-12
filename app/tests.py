import datetime
from types import SimpleNamespace

from django.contrib.auth.models import AnonymousUser
from django.template import Context, Template
from django.test import TestCase

from app.models import User


def render_perms_for_user(user):
    context = Context({'request': SimpleNamespace(user=user)})
    template_to_render = Template(
            '{% load perms %}'
            '{% perms %}'
    )
    rendered_template = template_to_render.render(context)
    return rendered_template


def render_bizz(num):
    context = Context({'num': num})
    template_to_render = Template(
            '{% load bizz %}'
            '{% bizz num %}'
    )
    rendered_template = template_to_render.render(context)
    return rendered_template


class TestCase(TestCase):
    def setUp(self):
        User.objects.create(username="test1", date_of_birth=datetime.date(2010, 1, 1))
        User.objects.create(username="test2", date_of_birth=datetime.date(1990, 1, 1))
        User.objects.create(username="test3")

    def test_perms(self):
        user1 = User.objects.get(username="test1")
        user2 = User.objects.get(username="test2")
        user3 = User.objects.get(username="test3")

        self.assertEqual(render_perms_for_user(user1), 'blocked')
        self.assertEqual(render_perms_for_user(user2), 'allowed')
        self.assertEqual(render_perms_for_user(user3), 'blocked')

        self.assertEqual(render_perms_for_user(AnonymousUser()), 'blocked')

    def test_fuzzbizz(self):
        self.assertEqual(render_bizz(1), '')
        self.assertEqual(render_bizz(3), 'Bizz')
        self.assertEqual(render_bizz(5), 'Fuzz')
        self.assertEqual(render_bizz(15), 'BizzFuzz')
        self.assertEqual(render_bizz(20), 'Fuzz')
