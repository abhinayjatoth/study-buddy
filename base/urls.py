from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerUser, name="register"),
    path('logout/', views.logoutPage, name="logout"),
    path('', views.home, name='home'), #Goes ot views flile and then home
    path('room/<str:pk>', views.room, name = 'room'), # name can help to redirec based on name 'url'
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>', views.deleteMessage, name="delete-message"),
]   