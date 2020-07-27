import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_status(client):
    response = client.get(reverse("post-list"))
    assert response.status_code == 200, "Should be status code 200"


@pytest.mark.django_db
@pytest.mark.parametrize(
    "user_username,user_email,user_password", [("test", "test@test.com", "test")]
)
def test_create_status(client, create_user, user_username, user_email, user_password):
    response = client.get(reverse("post-create"))
    assert response.status_code == 403, "Should be status code 403"
    create_user(user_username, user_email, user_password)
    assert client.login(username=user_username, password=user_password) is True
    response = client.get(reverse("post-create"))
    assert response.status_code == 200, "Should be status code 200"


@pytest.mark.django_db
@pytest.mark.parametrize("tag_title", ["test"])
@pytest.mark.parametrize(
    "post_title,post_tagline,post_body",
    [("test", "Here is a tagline", "# Here is a body title")],
)
def test_detail_status(
    client, create_tag, create_post, tag_title, post_title, post_tagline, post_body
):
    post = create_post(post_title, post_tagline, post_body)
    response = client.get(reverse("post-detail", args=[post.slug]))
    assert response.status_code == 200, "Should be status code 200"


@pytest.mark.django_db
@pytest.mark.parametrize("tag_title", [("test")])
@pytest.mark.parametrize(
    "post_title,post_tagline,post_body",
    [("test", "Here is a tagline", "# Here is a body title")],
)
@pytest.mark.parametrize(
    "user_username,user_email,user_password", [("test", "test@test.com", "test")]
)
def test_edit_status(
    client,
    create_tag,
    create_post,
    tag_title,
    post_title,
    post_tagline,
    post_body,
    create_user,
    user_username,
    user_email,
    user_password,
):
    post = create_post(post_title, post_tagline, post_body)
    response = client.get(reverse("post-edit", args=[post.pk]))
    assert response.status_code == 403, "Should be status code 403"
    create_user(user_username, user_email, user_password)
    assert client.login(username=user_username, password=user_password) is True
    response = client.get(reverse("post-edit", args=[post.pk]))
    assert response.status_code == 200, "Should be status code 200"
