from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.listpage, name='listpage'),
    path('post/<int:id>', views.detail, name="detail"),
    path('post/new/', views.create, name='post_new'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]