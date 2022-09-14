"""smw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from smwapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name = "home"),
    path('register/',views.registerpage, name = "register" ),
    path('login/', views.loginpage, name = "loginpage"),
    path('logout/', views.logoutpage, name = "logout"),
    path('addpost/', views.addpostview, name = "addpost"),
    path('post/<slug>', views.specific_post, name = "post"),
    path('like/<slug>', views.likedview, name = "like"),
    path('edit/<slug>', views.editpost, name = "editpost"),
    path('delete/<slug>', views.deletepost, name = 'delete'),
    path('deletecomment/<id>', views.deletecomment, name = 'deletecomment'),
    path('mytweets/', views.mytweets, name = 'mytweets'),
]
