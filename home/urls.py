from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import path
#from users.views import register



urlpatterns = [ 
    path('', views.index, name="home"),
    path('login', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    #path('Electronics.html/', views.Electronics, name="Electronics"),
    path('search/', views.search_view, name='search_view'),
    path('search/', views.search_view, name='search_view'),

    path('compare_prices/', views.compare_prices, name='compare_prices'), 
    path('Electronics/', views.Electronics, name='Electronics'),
    path('Fashion/', views.Fashion, name='Fashion'),
    path('Email/', views.Email, name='Email'),
    path('Sports/', views.Sports, name='Sports'),
    path('signup/', views.signup, name='signup'),
    #path('signup/', register, name='signup'),



    
]
