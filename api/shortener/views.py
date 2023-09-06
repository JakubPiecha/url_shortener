from typing import Any

from django.core.cache import cache
from django.views.generic import RedirectView
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from shortener import models, serializers
from shortener.serializers import URLSerializer


class CreateShortURLApiView(generics.CreateAPIView):
    """Create:
    Creates short URLs from original URL.
    Expected JSON data:
    example:
    {
        "url": "https://www.example.com/very/long/url/to/be/shortened"
    }
    Where url (string, required): The long URL that needs to be shortened.

    Response:
    Successful creation of a short URL, the API will respond with a JSON object containing the following information:

    short_url (string): The shortened URL that can be used to redirect to the original URL.
    Example:
    JSON DATA
    {
        "short_url": "https://salty-eyrie-21851-de0797a7d781.herokuapp.com/abcd123"
    }
    """

    queryset = models.URL.objects.all()
    serializer_class = serializers.OriginalURLSerializer

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = serializer.save()
        cache.set(url.short_url, url.url, timeout=60 * 60)

        short_url = URLSerializer(instance=url, context={"request": request})

        return Response(data=short_url.data, status=status.HTTP_201_CREATED)


class ShortUrlRedirectView(RedirectView):
    """
    get:
    Redirects the user to the original URL from the provided short URL.
    Expected the short URLto be part of the path, like:
    "https://salty-eyrie-21851-de0797a7d781.herokuapp.com/abcd123"
    Where "abcd123" is the short URL.

    The response is a HTTP 302 redirect to the original URL.
    """

    def get_redirect_url(self, *args: Any, short_url: str, **kwargs: Any) -> str | None:
        url = cache.get(short_url)

        if not url:
            instance = get_object_or_404(models.URL, short_url=short_url)
            cache.set(instance.short_url, instance.url, timeout=60 * 60)
            url = instance.url

        return url
