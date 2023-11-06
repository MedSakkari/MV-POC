from django.urls import path
from . import views

urlpatterns = [
    path('ai', views.MyApiView.as_view(), name='my-api'),
]
