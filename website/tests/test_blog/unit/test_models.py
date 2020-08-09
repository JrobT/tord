import pytest
import markdown
from django.template.defaultfilters import slugify
from profanity.validators import validate_is_profane
from blog.models import Tag, Post, Comment


@pytest.mark.django_db
@pytest.mark.parametrize("tag_title", ["test"])
@pytest.mark.parametrize(
    "post_title,post_tagline,post_body",
    [("test", "Here is a tagline", "# Here is a body title")],
)
def test_create_post(create_post, tag_title, post_title, post_tagline, post_body):
    # Create a Post and test the object and it's fields saved correctly.
    post = create_post(post_title, post_tagline, post_body)
    assert (
        Post.objects.filter(pk=post.pk).count() == 1
    ), "There should be a Post created"
    assert str(post) == post_title, "__str__ should be equal to title"
    assert slugify(post.title) in post.slug, "The Post's slug field needs to be set"


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
    # Create a Post and test the object's Markdown field.
    post = create_post(post_title, post_tagline, post_body)
    assert (
        markdown.markdown(post.body) == post_body_md
    ), "Markdown processing should be correct"


@pytest.mark.django_db
@pytest.mark.parametrize("tag_title", ["test"])
@pytest.mark.parametrize(
    "post_title1,post_title2,post_tagline,post_body",
    [("test1", "test2", "Here is a tagline", "# Here is a body title")],
)
def test_create_pinned_post(
    create_post, tag_title, post_title1, post_title2, post_tagline, post_body
):
    # Create a Post and test the object and it's fields saved correctly.
    post1 = create_post(post_title1, post_tagline, post_body)
    assert (
        Post.objects.filter(pk=post1.pk).count() == 1
    ), "There should be a Post created"
    assert str(post1) == post_title1, "__str__ should be equal to title"
    assert slugify(post1.title) in post1.slug, "The Post's slug field needs to be set"

    post2 = create_post(post_title2, post_tagline, post_body)
    assert (
        Post.objects.filter(pk=post2.pk).count() == 1
    ), "There should be a Post created"
    assert str(post2) == post_title2, "__str__ should be equal to title"
    assert slugify(post2.title) in post2.slug, "The Post's slug field needs to be set"

    # Test 'pinned' status is unique.
    assert Post.objects.filter(pinned=True).count() == 0
    temp = Post.objects.get(pk=post1.pk)
    temp.pinned = True
    temp.save()
    assert Post.objects.get(pinned=True) == post1
    temp = Post.objects.get(pk=post2.pk)
    temp.pinned = True
    temp.save()
    assert Post.objects.get(pinned=True) == post2


@pytest.mark.django_db
@pytest.mark.parametrize("tag_title,tag_background", [("test", "#222")])
def test_create_tag(create_tag, tag_title, tag_background):
    # Create a Tag and test the object and it's fields saved correctly.
    tag = create_tag(tag_title, tag_background)
    assert Tag.objects.filter(pk=tag.pk).count() == 1, "There should be a Tag created"
    assert str(tag) == tag_title, "__str__ should be equal to title"
    assert (
        slugify(tag.title) in tag.slug
    ), "The Tag's slug field needs to be set correctly"
    assert (
        tag.background == tag_background
    ), "The Tag's background needs to be set correctly"


@pytest.mark.django_db
@pytest.mark.parametrize(
    "comment_name, comment_email, comment_comment",
    [("test", "email@email.com", "This is a comment")],
)
@pytest.mark.parametrize(
    "post_title,post_tagline,post_body",
    [("test", "Here is a tagline", "# Here is a body title")],
)
def test_create_comment(
    create_comment,
    create_post,
    comment_name,
    comment_email,
    comment_comment,
    post_title,
    post_tagline,
    post_body,
):
    # Create a Post and test the object and it's fields saved correctly.
    post = create_post(post_title, post_tagline, post_body)
    assert (
        Post.objects.filter(pk=post.pk).count() == 1
    ), "There should be a Post created"
    assert str(post) == post_title, "__str__ should be equal to title"
    assert slugify(post.title) in post.slug, "The Post's slug field needs to be set"

    # Create a Comment and attach Post object.
    comment = create_comment(comment_name, comment_email, comment_comment, post=post)
    assert (
        Comment.objects.filter(pk=comment.pk).count() == 1
    ), "There should be a Comment created"
    assert str(comment) == "Comment {} by {}".format(
        comment.comment, comment.name
    ), "__str__ should be equal to comment structure"
    validate_is_profane(comment.name)
    validate_is_profane(str(comment))

    # Test 'Active' comments on Post object.
    assert Post.objects.get(pk=post.pk).active_comments.count() == 0
    temp = Comment.objects.get(pk=comment.pk)
    temp.active = True
    temp.save()
    assert Post.objects.get(pk=post.pk).active_comments.count() == 1
