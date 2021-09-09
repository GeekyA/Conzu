from django.urls import path
from .views import show_news
from . import views
urlpatterns = [
    path('',show_news, name="show_news"),
    path('aboutus', views.aboutus, name="aboutus")
]