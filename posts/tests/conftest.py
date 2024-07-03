import pytest

from posts.tests.factories import PostFactory


@pytest.fixture
def one_post():
    return PostFactory()
