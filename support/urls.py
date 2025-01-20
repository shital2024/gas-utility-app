from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='support_dashboard'),
    path('manage/<int:pk>/', views.manage_request, name='manage_request'),
]
