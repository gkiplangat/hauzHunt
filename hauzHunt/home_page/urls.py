from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home_page/', views.members, name='home_page'),
    path('home_page/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]