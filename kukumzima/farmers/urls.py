from django.urls import path

from . import views

urlpatterns = [

    path("", views.landing, name="landing"),
    path("home", views.home, name="home"),
    path('about/', views.about, name='about'),
    path('farm/', views.farm, name='farm'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('landingPage/', views.landing, name='landing')
]