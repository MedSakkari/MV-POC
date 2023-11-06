from django.urls import path
from . import views

urlpatterns = [
    path('user', views.MyApiView.as_view(), name='my-api'),
]
