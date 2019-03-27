from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.PollList.as_view(), name='PollList'),
    path('poll/<int:pk>', views.PollDetail.as_view(), name='PollDetail')
]
