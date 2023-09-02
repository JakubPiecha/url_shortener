import shortuuid
from rest_framework import serializers
from . import models
from .models import URL


class URLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = models.URL
        fields = ("short_url",)

    def get_short_url(self, obj):
        return self.context.get("request").build_absolute_uri("/") + obj.short_url


class OriginalURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.URL
        fields = ("url",)

    def save(self):
        original_url = self.validated_data.get("url")
        url = URL(url=original_url, short_url=shortuuid.uuid(name=original_url))
        url.save()
        return url
