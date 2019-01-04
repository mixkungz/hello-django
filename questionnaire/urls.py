from django.urls import path
from . import views

urlpatterns = [
    path('', views.init_page, name='Initial Page'),
]