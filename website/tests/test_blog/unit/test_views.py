import pytest
import markdown
from django.apps import apps
from django.urls import reverse
from blog.apps import BlogConfig
from blog.models import Category, Post


@pytest.fixture
def create_category():

    created_categories = []

    def _make_create_category(title):
        category = Category(title=title)
        created_categories.append(category)
        return category

    yield _make_create_category


@pytest.fixture
def create_post():

    created_posts = []

    def _make_create_post(title, body, category):
        post = Post(title=title, body=body, category=category)
        created_posts.append(post)
        return post

    yield _make_create_post


def test_blog_app():
    assert BlogConfig.name == "blog"
    assert apps.get_app_config("blog").name, "blog"


@pytest.mark.django_db
def test_index_status(client):
    response = client.get(reverse("post-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_status(client):
    response = client.get(reverse("post-create"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_post(create_category, create_post):
    category = create_category("Test")
    assert isinstance(category, Category)
    assert category.title == "Test"
    post = create_post("Test 1", "# Here is a body title", category)
    assert isinstance(post, Post)
    assert post.title == "Test 1"
    assert markdown.markdown(post.body) == "<h1>Here is a body title</h1>"
