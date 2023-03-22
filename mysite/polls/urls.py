# urls.py maps the views to a URL so they can be called

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]