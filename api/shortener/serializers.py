from rest_framework import serializers
from . import models


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.URL
        fields = (
            "id",
            "short_url",
        )


class OriginalURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.URL
        fields = ("original_url",)
