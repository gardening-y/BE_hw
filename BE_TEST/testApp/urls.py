from django.urls import path
from .views import *

urlpatterns = [
  path('', index , name='index'),
  path('create/', create , name='create'),
  path('detail/<int:pk>/', detail , name='detail'),
]
