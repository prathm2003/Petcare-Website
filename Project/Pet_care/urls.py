"""
URL configuration for Pet_care project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('homepage/',views.homepage,name='homepage'),
    path('services/',views.services,name = 'services'),
    path('testimonials/',views.testimonials,name = 'testimonials'),
    path('contact/',views.contact,name = 'contact'),
    path('contact/submit/', views.submit_contact_form, name='submit_contact_form'),
    path('logout/',views.logout1,name='logout1')

    # path('pet/', include('Pet_app.urls')),
]
