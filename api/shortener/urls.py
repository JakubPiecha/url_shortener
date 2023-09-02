from django.urls import path
from . import views

app_name = "shortener"

urlpatterns = [
    path("urls/", views.CreateShortURLApiView.as_view(), name="shorten_url"),
]
