from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('user/', views.userPage, name='user-page'),

    path('account/', views.accountSettings, name='account'),
    path('about/', views.aboutUs, name='about'),
    path('contact/', views.contactUs, name='contact'),

    path('messages/', views.viewMessages, name='messages'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    path('pets/', PetListView.as_view(), name='pet_list'),
    path('pets/<int:pk>/', PetDetailView.as_view(), name='pet_detail'),
    path('pets/new/', PetCreateView.as_view(), name='pet_create'),
    path('pets/<int:pk>/update/', PetUpdateView.as_view(), name='pet_update'),
    path('pets/<int:pk>/delete/', PetDeleteView.as_view(), name='pet_delete'),
]