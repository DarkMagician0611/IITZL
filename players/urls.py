from django.urls import path
from . import views

app_name = 'players'

urlpatterns = [
	path('', views.playerList, name='player_list'),
	path('create/', views.createPlayer, name='player_create'),
	path('add/', views.addPlayer, name='addPlayer'),
	path('delete/<pk>/', views.PlayerDelete.as_view(), name='player_delete'),
	path('<pk>/', views.PlayerDetail.as_view(), name='player_detail'),
]