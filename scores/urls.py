from django.urls import path
from . import views

app_name = 'scores'

urlpatterns = [
	path('', views.index, name='index'),
	path('bowling/', views.BallList.as_view(), name='bowling'),
	path('batting/', views.BatList.as_view(), name='batting'),
	path('fielding/', views.FieldList.as_view(), name='fielding'),
	path('playing/', views.PlayedList.as_view(), name='playing'),
	path('createBat/', views.createBat, name='createBat'),
	path('createBall/', views.createBall, name='createBall'),
	path('createField/', views.createField, name='createField'),
	path('createPlay/', views.createPlay, name='createPlay'),
	path('addBat/', views.addBat, name='addBat'),
	path('addBall/', views.addBall, name='addBall'),
	path('addField/', views.addField, name='addField'),
	path('addPlay/', views.addPlay, name='addPlay'),
	path('batDelete/<pk>/', views.BatDelete.as_view(), name='batDelete'),
	path('ballDelete/<pk>/', views.BallDelete.as_view(), name='ballDelete'),
	path('fieldDelete/<pk>/', views.FieldDelete.as_view(), name='fieldDelete'),
	path('playDelete/<pk>/', views.PlayDelete.as_view(), name='playDelete'),
	path('loadPlayer/', views.loadPlayer, name='loadPlayer'),
]