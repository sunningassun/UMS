"""
URL configuration for django1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name='index'),
    path('news/',views.news,name="news"),
    path('user/',views.user,name="user"),
    path('login/',views.login,name="login"),
    path('orm/',views.orm,name="orm"),


    path('add/',views.add,name='add'),
    path('delete/',views.delete,name='delete'),
    path('list/',views.list,name='list'),

    path('layout/',views.layout,name='layout'),
    path('depart/list/',views.depart_list,name='depart_list'),
    path('depart/add/',views.depart_add,name='depart_add'),
    path('depart/del/',views.depart_del,name='depart_del'),
    path('depart/<int:nid>/edit/',views.depart_edit,name='depart_edit'),
    path('user/list/',views.user_list,name='user_list'),
    path('user/add/',views.user_add,name='user_add'),
    path('user/modelform/add/',views.user_modelform_add,name='user_modelform_add'),
    # path('user/<int:nid>/>edit/',views.edit,name='user_edit'),
]

