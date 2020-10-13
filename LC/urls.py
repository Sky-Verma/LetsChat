from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('loginForm/',views.login_request,name='loginForm'),
    path('chats/',views.chats,name='chats'),
    path('my_profile/',views.my_profile,name='my_profile'),
    path('users/',views.users,name='users'),
    path('logout/',views.logout_view,name='logout')
]
