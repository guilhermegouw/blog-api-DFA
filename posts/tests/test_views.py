import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from posts.models import Post


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_post_list_create(api_client, one_post, user):
    # Authenticate the API client
    login_success = api_client.login(
        username=user.username, password="testpassword"
    )
    assert login_success  # Ensure the login was successful

    # Test GET request
    url = reverse("post_list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["title"] == one_post.title

    # Test POST request
    post_data = {
        "title": "New Post",
        "body": "This is a new post.",
        "author": user.id,  # Use user ID instead of the user object
    }
    response = api_client.post(url, post_data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Post.objects.count() == 2
    assert Post.objects.latest("id").title == "New Post"


@pytest.mark.django_db
def test_post_detail_as_admin(api_client, one_post, admin_user):
    api_client.force_authenticate(user=admin_user)
    url = reverse("post_detail", kwargs={"pk": one_post.id})

    # Test GET request
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == one_post.title

    # Test PUT request
    updated_data = {
        "title": "Updated Post",
        "body": one_post.body,
        "author": one_post.author.id,
    }
    response = api_client.put(url, updated_data, format="json")
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_post_detail_as_author(api_client, one_post, user):
    api_client.force_authenticate(user=user)  # one_post.author = user
    url = reverse("post_detail", kwargs={"pk": one_post.id})

    # Test GET request
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == one_post.title

    # Test PUT request
    updated_data = {
        "title": "Updated Post",
        "body": one_post.body,
        "author": one_post.author.id,
    }
    response = api_client.put(url, updated_data, format="json")
    assert response.status_code == status.HTTP_200_OK

    # Test DELETE request
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
