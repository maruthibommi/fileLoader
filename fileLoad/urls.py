from django.urls import path
from fileLoad import views

urlpatterns = [
    path("", views.hello_there, name="home"),
]