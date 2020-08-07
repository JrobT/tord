import pytest
from blog.forms import CommentForm, EmailForm
from blog.models import Post, Comment, Email


@pytest.mark.django_db
@pytest.mark.parametrize(
    "post_title, post_tagline, post_body",
    [("test", "Here is a tagline", "# Here is a body title")],
)
@pytest.mark.parametrize(
    "comment_name, comment_email, comment_comment, comment_parent, expected_result",
    [
        ("test", "email@email.com", "This is a comment", False, True),
        ("", "test", "This is a comment", False, False),
        ("test", "email@email.com", "This is a comment", True, False),
    ],
)
def test_comment_form(
    create_comment,
    create_post,
    post_title,
    post_tagline,
    post_body,
    comment_name,
    comment_email,
    comment_comment,
    comment_parent,
    expected_result,
):
    """Test comment form validation."""
    # Create two Posts.
    post1 = create_post(post_title, post_tagline, post_body)
    post2 = create_post(post_title + "2", post_tagline, post_body)
    assert Post.objects.all().count() == 2, "There should be two Posts created"

    # Create a Comment and attach to first Post object.
    comment = create_comment(comment_name, comment_email, comment_comment, post=post1)
    assert Comment.objects.all().count() == 1, "There should be a Comment created"

    # Assert form input is expected result.
    form = CommentForm(
        data={
            "name": comment_name,
            "email": comment_email,
            "comment": comment_comment,
            "post": post2,
            "parent": comment.pk if comment_parent else None,
        }
    )
    assert form.is_valid() == expected_result


@pytest.mark.django_db
@pytest.mark.parametrize(
    "email_address, expected_result",
    [("test", False), ("test@test.com", True), ("already@accepted.com", False)],
)
def test_email_form(create_email, email_address, expected_result):
    """Test email form validation."""
    # Create an Email.
    email = create_email("already@accepted.com")
    assert (
        Email.objects.filter(pk=email.pk).count() == 1
    ), "There should be a Email created"

    # Assert form input is expected result.
    form = EmailForm(data={"email": email_address})
    assert form.is_valid() == expected_result
