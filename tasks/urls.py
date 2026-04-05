from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home),
    path('', views.home, name='home'),
    path('api/tasks/', views.api_tasks),
]