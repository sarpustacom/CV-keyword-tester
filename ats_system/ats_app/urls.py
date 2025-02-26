from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("form/", views.form_view, name="form"),
    path("check/", views.check_view, name="check")
]