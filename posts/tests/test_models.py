import pytest


@pytest.mark.django_db
def test_post_model(one_post):
    assert one_post.title
    assert one_post.body
    assert one_post.author
    assert one_post.created_at
    assert one_post.updated_at
    assert str(one_post) == one_post.title
