from django.urls import path
from .views import managementrecords, new_hotel, login_view, logout_view

app_name = "new_hotel"

urlpatterns =[
     path('', new_hotel, name="new_hotel"),
     path('login', login_view, name="login"),
     path('logout', logout_view, name="logout"),
     path('managementrecords', managementrecords, name='managementrecords')
]