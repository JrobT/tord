import pytest
from django.apps import apps
from django.urls import reverse
from blog.apps import BlogConfig


def test_blog_app():
    assert BlogConfig.name == "blog"
    assert apps.get_app_config("blog").name, "blog"


@pytest.mark.django_db
def test_index_status(client):
    response = client.get(reverse("post-list"))
    assert response.status_code == 200, "Should be status code 200"


@pytest.mark.django_db
def test_create_status(client):
    response = client.get(reverse("post-create"))
    assert response.status_code == 200, "Should be status code 200"


@pytest.mark.django_db
@pytest.mark.parametrize("category_title", ["test"])
@pytest.mark.parametrize("post_title,post_body", [("test", "# Here is a body title")])
def test_detail_status(
    client, create_category, create_post, category_title, post_title, post_body
):
    category = create_category(category_title)
    post = create_post(post_title, post_body, category)
    response = client.get(reverse("post-view", args=[post.slug]))
    assert response.status_code == 200, "Should be status code 200"


@pytest.mark.django_db
@pytest.mark.parametrize("category_title", [("test")])
@pytest.mark.parametrize("post_title,post_body", [("test", "# Here is a body title")])
def test_edit_status(
    client, create_category, create_post, category_title, post_title, post_body
):
    category = create_category(category_title)
    post = create_post(post_title, post_body, category)
    response = client.get(reverse("post-edit", args=[post.pk]))
    assert response.status_code == 200, "Should be status code 200"
