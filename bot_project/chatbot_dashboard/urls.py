from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.MyApiView.as_view(), name='my-api'),
]
