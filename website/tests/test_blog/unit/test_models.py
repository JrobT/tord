import pytest
import markdown
from django.template.defaultfilters import slugify
from blog.models import Category, Post


@pytest.mark.django_db
@pytest.mark.parametrize("category_title", ["test"])
def test_create_category(create_category, category_title):
    category = create_category(category_title)
    assert (
        Category.objects.filter(pk=category.pk).count() == 1
    ), "There should be the object created in the database"
    assert str(category) == category_title, "__str__ should be equal to title"
    assert (
        slugify(category.title) == category.slug
    ), "The object's slug field needs to be set"


@pytest.mark.django_db
@pytest.mark.parametrize("category_title", ["test"])
@pytest.mark.parametrize("post_title,post_body", [("test", "Here is a body title")])
def test_create_post(
    create_category, category_title, create_post, post_title, post_body
):
    category = create_category(category_title)
    post = create_post(post_title, post_body, category)
    assert (
        Post.objects.filter(pk=post.pk).count() == 1
    ), "There should be the object created in the database"
    assert str(post) == post_title, "__str__ should be equal to title"
    assert slugify(post.title) == post.slug, "The object's slug field needs to be set"


@pytest.mark.django_db
@pytest.mark.parametrize("category_title", ["test"])
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
def test_post_body(
    create_category, category_title, create_post, post_title, post_body, post_body_md
):
    category = create_category(category_title)
    post = create_post(post_title, post_body, category)
    assert (
        markdown.markdown(post.body) == post_body_md
    ), "Markdown processing should be correct"
