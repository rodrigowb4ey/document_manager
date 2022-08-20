import random

from django.contrib.auth.models import User


def get_random_user():
    return random.choice(User.objects.all())
