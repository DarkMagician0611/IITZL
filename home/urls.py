from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
	path('', views.index, name='index'),
	path('admin/', views.admin, name='admin'),
	path('players/', views.players, name='players'),
	path('team/', views.team, name='team'),
	path('scores/', views.scores, name='scores'),
	path('leaderboard/', views.leaderboard, name='leaderboard'),
	path('rules/', views.rules, name='rules'),
]