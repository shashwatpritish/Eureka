from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("delete/<str:note>", views.delete, name="Delete"),
]