from django.urls import path
from fileLoad import views

urlpatterns = [
    path("", views.home, name="home"),
]