from django.urls import path

from . import views

urlpatterns = [

    path("home/", views.home1, name="home1"),
    path("about/",views.about1, name="about1"),
    path("orderHistory/",views.orderHistory, name="orderHistory"),
    path('login/', views.login1, name='login1'),
    path('signup/', views.signup1, name='signup1'),
    path('landingPage/', views.landing1, name='landing1'),
    
    path('buyer/', views.buyer_list, name='buyer_list'),
    path("order/",views.order, name="order"),
]

