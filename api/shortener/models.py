from django.db import models

# Create your models here.


class URL(models.Model):
    url = models.CharField(max_length=2000)
    short_url = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "URL"
        verbose_name_plural = "URLs"

    def __str__(self):
        return f"{self.url[:30]} -> {self.short_url}"
