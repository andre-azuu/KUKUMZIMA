from django.urls import path

from . import views

from .views import farmer_list, farmer_detail, farmer_create, farmer_update, farmer_delete


urlpatterns = [

    path("", views.landing, name="landing"),
    path("home", views.home, name="home"),
    path('about/', views.about, name='about'),
    path('farm/', views.farm, name='farm'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('landingPage/', views.landing, name='landing'),


    path('farmerslist/', views.farmer_list, name='farmer_list'),
    path('farmers/<int:pk>/', farmer_detail, name='farmer_detail'),
    path('farmers/create/', farmer_create, name='farmer_create'),
    path('farmers/<int:pk>/update/', farmer_update, name='farmer_update'),
    path('farmers/<int:pk>/delete/', farmer_delete, name='farmer_delete'),

]