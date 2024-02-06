from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home.as_view(),name='home'),
    path("register/",views.Register.as_view(),name='register'),
    path("login/",views.Login.as_view(),name='login'),
    path("dashboard/",views.dashboard.as_view,name='dasboard'),
   
]
