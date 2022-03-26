from django.contrib import admin
from django.urls import path,include
from crudApp import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',include('crudApp.urls')),
]