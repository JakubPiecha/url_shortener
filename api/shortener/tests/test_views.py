import shortuuid
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework import status

from shortener.models import URL
from shortener.views import ShortUrlRedirectView


def test_create_short_url(api_client, db):
    url = "/api/v1/urls/"
    data = {"url": "https://test.com.pl"}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert URL.objects.get(url="https://test.com.pl").short_url == shortuuid.uuid("https://test.com.pl")


def test_create_short_url_wrong_url(api_client, db):
    url = reverse("shortener:shorten_url")
    data = {"url": "testcompl"}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'Enter a valid URL.' in response.data["url"]
    assert len(URL.objects.all()) == 0


def test_create_short_url_this_same_data(api_client, sample_url):
    url = reverse("shortener:shorten_url")
    data = {"url": "http://www.example.com"}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert URL.objects.get(url="http://www.example.com").short_url == sample_url.short_url
    assert len(URL.objects.all()) == 1


def test_redirect_existing_short_url(api_client, sample_url):
    short_url = sample_url.short_url
    url = reverse("shortener:redirect", args=[short_url])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == "http://www.example.com"


def test_redirect_not_existing_short_url(api_client, sample_url):
    short_url = "nonexistent"
    url = reverse("shortener:redirect", args=[short_url])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_cache_hit(sample_url, *args, **kwargs):
    short_url = sample_url.short_url
    url = cache.get(short_url)

    assert url == "http://www.example.com"


def test_cache_miss(sample_url, api_client):
    cache.clear()
    short_url = sample_url.short_url
    url_cache_before = cache.get(short_url)
    url = reverse("shortener:redirect", args=[short_url])
    response = api_client.get(url)
    url_cache_after = cache.get(short_url)

    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == "http://www.example.com"
    assert url_cache_before == None
    assert url_cache_after == 'http://www.example.com'
