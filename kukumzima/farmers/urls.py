from django.urls import path

from .views import landing,home,about,farm,login,signup

from .views import farmer_list, farmer_detail, farmer_create, farmer_update, farmer_delete
from .views import farm_list, farm_detail, farm_create, farm_update, farm_delete
from .views import inventory_list, inventory_detail, inventory_update,inventory_create,inventory_delete
from .views import transaction_list, transaction_detail, transaction_create, transaction_update, transaction_delete


urlpatterns = [

    path("", landing, name="landing"),
    path("home/", home, name="home"),
    path('about/',about, name='about'),
    path('farm/', farm, name='farm'),
    path('login/', login, name='login'),
    path('signup/',signup, name='signup'),
    path('landingPage/',landing, name='landing'),

# farmers
    path('farmerslist/',farmer_list, name='farmer_list'),
    path('farmers/<int:pk>/',farmer_detail, name='farmer_detail'),
    path('farmers/create/',farmer_create, name='farmer_create'),
    path('farmers/<int:pk>/update/', farmer_update, name='farmer_update'),
    path('farmers/<int:pk>/delete/',farmer_delete, name='farmer_delete'),

# farms
    path('farms/', farm_list, name='farm_list'),
    path('farms/<int:pk>/', farm_detail, name='farm_detail'),
    path('farms/create/', farm_create, name='farm_create'),
    path('farms/<int:pk>/update/', farm_update, name='farm_update'),
    path('farms/<int:pk>/delete/', farm_delete, name='farm_delete'),


# inventory

    path('inventory/', inventory_list, name='inventory_list'),
    path('inventory/<int:pk>/', inventory_detail, name='inventory_detail'),
    path('inventory/<int:pk>/update/', inventory_update, name='inventory_update'),

    path('inventory/create/', inventory_create, name='inventory_create'),
    path('inventory/<int:pk>/delete/', inventory_delete, name='inventory_delete'),


# transactions
    path('transactions/', transaction_list, name='transaction_list'),
    path('transactions/<int:pk>/', transaction_detail, name='transaction_detail'),
    path('transactions/create/', transaction_create, name='transaction_create'),
    path('transactions/<int:pk>/update/', transaction_update, name='transaction_update'),
    path('transactions/<int:pk>/delete/', transaction_delete, name='transaction_delete'),
    ]


