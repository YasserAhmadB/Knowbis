from rest_framework.test import APIClient
import pytest

from _platform.models import Provider, Audience
from authenticator.models import User
from model_bakery import baker


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticate(api_client):
    def do_authenticate(is_staff=False):
        return api_client.force_authenticate(user=User(is_staff=is_staff))
    return do_authenticate


@pytest.fixture
def authenticate_provider(api_client):
    def do_authenticate():
        user = baker.make(User)
        _ = api_client.force_authenticate(user=user)
        provider = baker.make(Provider, user_id=user.id)
        return provider
    return do_authenticate


@pytest.fixture
def authenticate_audience(api_client):
    def do_authenticate():
        user = baker.make(User)
        _ = api_client.force_authenticate(user=user)
        audience = baker.make(Audience, user_id=user.id)
        return _
    return do_authenticate
