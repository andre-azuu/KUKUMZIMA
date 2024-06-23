from django.urls import path

from . import views

from .views import farmer_list, farmer_detail, farmer_create, farmer_update, farmer_delete
from .views import farmer_list, farmer_detail, farmer_create, farmer_update, farmer_delete,farm_list, farm_detail, farm_create, farm_update, farm_delete


urlpatterns = [

    path("", views.landing, name="landing"),
    path("home", views.home, name="home"),
    path('about/', views.about, name='about'),
    path('farm/', views.farm, name='farm'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('landingPage/', views.landing, name='landing'),

# farmers
    path('farmerslist/', views.farmer_list, name='farmer_list'),
    path('farmers/<int:pk>/', views.farmer_detail, name='farmer_detail'),
    path('farmers/create/', views.farmer_create, name='farmer_create'),
    path('farmers/<int:pk>/update/', views.farmer_update, name='farmer_update'),
    path('farmers/<int:pk>/delete/', views.farmer_delete, name='farmer_delete'),

# farms
    path('farms/', farm_list, name='farm_list'),
    path('farms/<int:pk>/', farm_detail, name='farm_detail'),
    path('farms/create/', farm_create, name='farm_create'),
    path('farms/<int:pk>/update/', farm_update, name='farm_update'),
    path('farms/<int:pk>/delete/', farm_delete, name='farm_delete'),

]