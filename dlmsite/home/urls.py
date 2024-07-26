from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("simple_form_view", views.simple_form_view, name="simple_form_view"),
    path("download", views.download, name="download"),
]