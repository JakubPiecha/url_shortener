from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
