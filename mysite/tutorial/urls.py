from django.urls import path
from .views import *

urlpatterns = [
    path('', tutorial_page)
]