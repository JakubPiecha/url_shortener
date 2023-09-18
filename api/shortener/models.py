
from django.db import models


class URL(models.Model):
    url = models.URLField(max_length=2000)
    short_url = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "URL"
        verbose_name_plural = "URLs"

    def __str__(self):
        return f"{self.url[:30]} -> {self.short_url}"

    def save(self, *args, **kwargs):
        if not len(URL.objects.filter(short_url=self.short_url)):
            super().save(*args, **kwargs)


