import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_login_page_accessible(api_client):
    url = reverse("rest_framework:login")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_user_can_login_with_valid_credentials(api_client, user):
    url = reverse("rest_framework:login")
    data = {"username": user.username, "password": user.password}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_user_cannot_login_with_invalid_credentials(api_client):
    url = reverse("custom_login")
    data = {"username": "invalid", "password": "invalid"}
    response = api_client.post(url, data, format="json")
    print(response.content)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "non_field_errors" in response.data
    assert response.data["non_field_errors"] == [
        "Unable to log in with provided credentials."
    ]
