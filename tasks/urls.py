from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('createTask/', views.createTask, name='createTask'),
    path('editTask/<id>', views.editTask, name='editTask'),
    path('deleteTask/<id>', views.deleteTask, name='deleteTask'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
