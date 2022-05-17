from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logOutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="userProfile"),
    path('create-room/', views.createRoom, name="createRoom"),
    path('update-room/<str:pk>/', views.updateRoom, name="updateRoom"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="deleteRoom"),
    path('delete-message/<int:pkRoom>/<str:pk>/',
         views.deleteMessage, name="deleteMessage"),
    path('delete-message/<str:pk>/',
         views.deleteMessageinFeed, name="deleteMessageinFeed"),
]
