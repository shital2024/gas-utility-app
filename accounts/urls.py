from django.urls import path
from . import views

urlpatterns = [
    path('details/', views.account_details, name='account_details'),
]
