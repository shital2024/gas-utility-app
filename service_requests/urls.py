from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_request, name='create_request'),
    path('status/<int:pk>/', views.request_status, name='request_status'),
]
