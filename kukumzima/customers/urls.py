from django.urls import path

from . import views

urlpatterns = [

    path("home/", views.home1, name="home1"),
    path("about/",views.about1, name="about1"),
    path("order/",views.order, name="order"),
    path("orderHistory/",views.orderHistory, name="orderHistory"),
    path('login/', views.login1, name='login1'),
    path('signup/', views.signup1, name='signup1'),
    path('landingPage/', views.landing1, name='landing1')
    
]