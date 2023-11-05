"""userproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    #path("Electronics/",include('Electronics.urls')),
    path('search/', views.search_view, name='search_view'),
    path('search/', views.search_products, name='search_products'),
    path('Electronics/', views.Electronics, name='Electronics'),
    path('Fashion/', views.Fashion, name='Fashion'),
    path('Email/', views.Email, name='Email'),
      path('search/', views.search_view, name='search_view'),
      path('Sports/', views.Sports, name='Sports'),
      #path('signup/', include('home.urls')), 
      
    
]
