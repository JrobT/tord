import json
import django
import pytest
from os import getenv
from django.conf import settings
from django.contrib.auth.models import User
from blog.models import Category, Post


def pytest_configure():
    settings.DEBUG = False
    django.setup()


@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": getenv("DATABASE_ENGINE", "django.db.backends.postgresql_psycopg2"),
        "NAME": getenv("DATABASE_NAME", "truteordare"),
        "USER": getenv("DATABASE_USERNAME", "truteordare"),
        "PASSWORD": getenv("DATABASE_PASSWORD", "truteordare"),
        "HOST": getenv("DATABASE_HOST", "127.0.0.1"),
        "PORT": getenv("DATABASE_PORT", "5432"),
        "OPTIONS": json.loads(getenv("DATABASE_OPTIONS", "{}")),
    }


@pytest.fixture
def create_category():

    created_categories = []

    def _make_create_category(title):
        category = Category(title=title)
        category.save()
        created_categories.append(category)
        return category

    yield _make_create_category

    for category in created_categories:
        category.delete()


@pytest.fixture
def create_post():

    created_posts = []

    def _make_create_post(title, body, category):
        post = Post(title=title, body=body, category=category)
        post.save()
        created_posts.append(post)
        return post

    yield _make_create_post

    for post in created_posts:
        post.delete()


@pytest.fixture
def create_user():

    created_users = []

    def _make_create_user(username, email, password):
        user = User.objects.create_superuser(
            username=username, email=email, password=password
        )
        user.save()
        created_users.append(user)
        return user

    yield _make_create_user

    for user in created_users:
        user.delete()
