from django.urls import path
from . import views

app_name = 'leaderboard'

urlpatterns = [
	path('', views.index, name='index'),
	path('calculateScore/', views.calculateScore, name='calculateScore'),
	path('matchNumber/', views.matchNumber, name='matchNumber'),
	path('profile/', views.profile, name='profile'),
]