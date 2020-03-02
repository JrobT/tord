import json
import django
import pytest
from os import getenv
from django.conf import settings


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
