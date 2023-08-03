from django.urls import path
from . import views

urlpatterns = [
    path('HomeContext/',views.HomeContext,name='HomeContext')
]
