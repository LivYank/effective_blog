from django.urls import path
from . import viewsn

urlpatterns = [
    path('', views.post_list, name='post_list'),
]