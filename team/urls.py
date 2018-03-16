from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [
	path('', views.selectMatch, name='selectMatch'),
	path('index/', views.index, name='index'),
	path('teamAddIndex/', views.teamAddIndex, name='teamAddIndex'),
	path('playerAdd/', views.playerAdd, name='playerAdd'),
	path('addPlayerLater/', views.addPlayerLater, name='addPlayerLater'),
	path('addBlackMamba/', views.addBlackMamba, name='addBlackMamba'),
	path('loadPlayer/', views.loadPlayer, name='loadPlayer'),
	path('updateMamba/', views.updateMamba, name='updateMamba'),
	path('update/<str:name>/', views.update, name='update'),
	path('deleteTeamPlayer/<str:name>/', views.deleteTeamPlayer, name='deleteTeamPlayer'),
	path('playerUpdate/', views.playerUpdate, name='playerUpdate'),
	path('resetTeam/', views.resetTeam, name='resetTeam'),
]