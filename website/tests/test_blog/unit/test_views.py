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
@pytest.mark.parametrize("category_title", ["test", "test_category"])
@pytest.mark.parametrize(
    "post_title,post_body,post_body_md",
    [
        ("test", "# Here is a body title", "<h1>Here is a body title</h1>"),
        (
            "test_post",
            "**Here is a body title**",
            "<p><strong>Here is a body title</strong></p>",
        ),
    ],
)
def test_detail_status(
    client,
    create_category,
    create_post,
    category_title,
    post_title,
    post_body,
    post_body_md,
):
    response = client.get(reverse("post-view", args=[post_title]))
    assert response.status_code == 404
    category = create_category(category_title)
    assert str(category) == category_title
    post = create_post(post_title, post_body, category)
    assert str(post) == post_title
    assert markdown.markdown(post.body) == post_body_md
    response = client.get(reverse("post-view", args=[post.slug]))
    assert response.status_code == 200
