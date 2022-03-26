from types import MethodType
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
# importing views from views..py
from .views import detail_view,create_view,list_view,delete_view,update_view
urlpatterns = [
    path('',list_view ),
    path('create',create_view ),
    path('details/<id>/',detail_view ),
    path('update/<id>',update_view),
    path('delete/<id>',delete_view),
]