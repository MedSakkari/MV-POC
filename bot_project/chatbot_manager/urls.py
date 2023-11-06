from django.urls import path
from . import views

urlpatterns = [
    path('bot-manager', views.MyApiView.as_view(), name='my-api'),
]
