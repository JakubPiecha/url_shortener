import pytest
import shortuuid
from django.contrib.auth import get_user_model

from shortener.models import URL
from rest_framework.test import APIClient


@pytest.fixture
def sample_url(db):
    return URL.objects.create(url="http://www.example.com", short_url=shortuuid.uuid(name="http://www.example.com"))


@pytest.fixture
def sample_user(db):
    user = get_user_model().objects.create_user(username="Test_user", email="a@a.pl", password="Test123456")
    return user


@pytest.fixture
def sample_long_url(db):
    return URL.objects.create(
        url="https://pytest-django.readthedocs.io/en/latest/tutorial.html#introduction",
        short_url=shortuuid.uuid(
            name="https://pytest-django.readthedocs.io/en/latest/tutorial.html#introduction"))


@pytest.fixture
def api_client():
    client = APIClient()
    return client
