from django.urls import path
from Pet_app import views
urlpatterns = [  
    path('home/', views.home),
]