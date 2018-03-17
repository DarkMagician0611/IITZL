from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserData
from team.models import Team, PlayerTeam
from scores.models import BatRecord, BallRecord, FieldRecord, PlayedRecord
# Create your views here.
def index(request):
	users = UserData.objects.all().order_by('points').reverse()
	context = {'users' : users}
	return render(request, 'leaderboard/index.html', context)

def matchNumber(request):
	matches = [1, 2]
	return render(request, 'leaderboard/calculate.html', {'matches' : matches})

def calculateScore(request):
	users = User.objects.filter(groups__name='Players')
	for user in users:
		u = UserData.objects.filter(user=user)
		if not u.exists():
			ud = UserData(user=user)
			ud.save()
	match = int(request.POST['match'])
	bat = BatRecord.objects.filter(match=match)
	ball = BallRecord.objects.filter(match=match)
	field = FieldRecord.objects.filter(match=match)
	play = PlayedRecord.objects.filter(match=match)
	for user in users:
		name = str(user) + ' match#' + str(match)
		team = Team.objects.filter(name=name)
		ud = UserData.objects.get(user=user)
		if team.exists():
			team = team[0]
			for x in bat:
				team_player = PlayerTeam.objects.filter(team=team, player=x.player)
				if team_player.exists():
					if x.player.name == team.black_mamba.name:
						ud.points += 2 * x.points
					else:
						ud.points += x.points
			for x in ball:
				team_player = PlayerTeam.objects.filter(team=team, player=x.player)
				if team_player.exists():
					if x.player.name == team.black_mamba.name:
						ud.points += 2 * x.points
					else:
						ud.points += x.points
			for x in field:
				team_player = PlayerTeam.objects.filter(team=team, player=x.player)
				if team_player.exists():
					if x.player.name == team.black_mamba.name:
						ud.points += 2 * x.points
					else:
						ud.points += x.points
			for x in play:
				team_player = PlayerTeam.objects.filter(team=team, player=x.player)
				if team_player.exists():
					ud.points += x.points
			ud.save()
	bat.delete()
	ball.delete()
	field.delete()
	play.delete()
	return redirect('/leaderboard/')

def profile(request):
	u = UserData.objects.filter(user=request.user)
	if not u.exists():
		ud = UserData(user=request.user)
		ud.save()
	u = u[0]
	return render(request, 'leaderboard/profile.html', {'u' : u})

def resetUsers(request):
	users = User.objects.filter(groups__name='Players')
	for user in users:
		u = UserData.objects.filter(user=user)
		if not u.exists():
			ud = UserData(user=user)
			ud.save()
		ud = UserData.objects.get(user=user)
		ud.points = 0
		ud.save()
	return redirect('/leaderboard/')