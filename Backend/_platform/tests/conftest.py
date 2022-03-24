from django.contrib.auth.models import User
from rest_framework.test import APIClient
import pytest


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticate():
    def do_authenticate(is_staff=False):
        return APIClient.force_authenticate(User(is_staff=is_staff))
    return do_authenticate
