import pytest
import markdown
from django.template.defaultfilters import slugify
from blog.models import Tag, Post


@pytest.mark.django_db
@pytest.mark.parametrize("tag_title", ["test"])
def test_create_tag(create_tag, tag_title):
    tag = create_tag(tag_title)
    assert (
        Tag.objects.filter(pk=tag.pk).count() == 1
    ), "There should be the object created in the database"
    assert str(tag) == tag_title, "__str__ should be equal to title"
    assert slugify(tag.title) == tag.slug, "The object's slug field needs to be set"


@pytest.mark.django_db
@pytest.mark.parametrize("tag_title", ["test"])
@pytest.mark.parametrize(
    "post_title,post_tagline,post_body",
    [("test", "Here is a tagline", "# Here is a body title")],
)
def test_create_post(
    create_tag, tag_title, create_post, post_title, post_tagline, post_body
):
    post = create_post(post_title, post_tagline, post_body)
    assert (
        Post.objects.filter(pk=post.pk).count() == 1
    ), "There should be the object created in the database"
    assert str(post) == post_title, "__str__ should be equal to title"
    assert slugify(post.title) == post.slug, "The object's slug field needs to be set"


@pytest.mark.django_db
@pytest.mark.parametrize("tag_title", ["test"])
@pytest.mark.parametrize(
    "post_title,post_tagline,post_body,post_body_md",
    [
        (
            "test",
            "Here is a tagline",
            "# Here is a body title",
            "<h1>Here is a body title</h1>",
        ),
        (
            "test",
            "Here is a tagline",
            "**Here is a body title**",
            "<p><strong>Here is a body title</strong></p>",
        ),
    ],
)
def test_post_body(
    create_tag,
    tag_title,
    create_post,
    post_title,
    post_tagline,
    post_body,
    post_body_md,
):
    post = create_post(post_title, post_tagline, post_body)
    assert (
        markdown.markdown(post.body) == post_body_md
    ), "Markdown processing should be correct"
