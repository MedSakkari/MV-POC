# chatbot_core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('core1', views.MyApiView.as_view(), name='c1'),
    path('core2', views.MyApiView.as_view(), name='c2'),
]
