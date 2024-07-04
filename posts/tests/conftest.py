import pytest

from accounts.tests.factories import UserFactory
from posts.tests.factories import PostFactory


@pytest.fixture
def one_post(user):
    return PostFactory(author=user)


@pytest.fixture
def user():
    return UserFactory(password="testpassword")


@pytest.fixture
def admin_user():
    return UserFactory(
        password="adminpassword", is_staff=True, is_superuser=True
    )
