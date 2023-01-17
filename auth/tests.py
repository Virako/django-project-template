import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient


User = get_user_model()


@pytest.mark.django_db
def test_valid_auth():
    user = User.objects.create_user("username", "me@test.com", "password")
    url = reverse("auth:token")
    client = APIClient()
    response = client.post(
        url,
        data={
            "username": user.username,
            "password": "password",
        },
    )
    assert response.status_code == 200
    assert "token" in response.json()
