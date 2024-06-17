from django.urls import path
from . views import *


urlpatterns = [
    path('loginuser/',userLogin,name='loginpage'),
    path('logoutuser/',userLogout,name='logoutpage'),
    path('registeruser/',userRegister,name='registerpage'),
    path('allusers/',allusers,name='allusersPage'),
    path('deleteuser/<user_id>',deleteUser,name='deleteuserPage'),
]


