from django.apps import apps
from landing.apps import LandingConfig
from blog.apps import BlogConfig


def test_landing_app():
    assert LandingConfig.name == "landing"
    assert apps.get_app_config("landing").name, "landing"


def test_blog_app():
    assert BlogConfig.name == "blog"
    assert apps.get_app_config("blog").name, "blog"
