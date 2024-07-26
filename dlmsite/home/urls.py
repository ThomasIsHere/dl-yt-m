from django.urls import path

from . import views

urlpatterns = [
    path("", views.simple_form_view, name="simple_form_view"),
]