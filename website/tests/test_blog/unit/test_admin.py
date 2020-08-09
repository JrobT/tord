import pytest
from blog.admin import CommentAdmin
from blog.models import Post, Comment


@pytest.mark.django_db
@pytest.mark.parametrize(
    "comment_name, comment_email, comment_comment",
    [("test", "email@email.com", "This is a comment")],
)
@pytest.mark.parametrize(
    "post_title,post_tagline,post_body",
    [("test", "Here is a tagline", "# Here is a body title")],
)
def test_approve_comments(
    create_comment,
    create_post,
    comment_name,
    comment_email,
    comment_comment,
    post_title,
    post_tagline,
    post_body,
):
    """Test mass approval of comments."""
    # Create a Post.
    post = create_post(post_title, post_tagline, post_body)
    assert Post.objects.all().count() == 1, "There should be a Post created"

    # Create a Comment and attach Post object.
    comment = create_comment(comment_name, comment_email, comment_comment, post=post)
    assert Comment.objects.all().count() == 1, "There should be a Comment created"

    # Assert comment is active after passing to `approve_comments()`.
    assert comment.active is False
    CommentAdmin.approve_comments(None, None, Comment.objects.all())
    assert Comment.objects.get(pk=comment.pk).active is True
