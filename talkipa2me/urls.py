from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='home'),
    path('issues', views.Issues.as_view(), name='issues'),
    path('what_is', views.WhatIs.as_view(), name='what_is')
]
