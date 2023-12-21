from django.urls import path

from . import views

urlpatterns = [
    path('home_page/', views.members, name='home_page'),
]