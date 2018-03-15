from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserData
from team.models import Team, PlayerTeam
from scores.models import BatRecord, BallRecord, FieldRecord
# Create your views here.
def index(request):
	users = UserData.objects.all()
	context = {'users' : users}
	return render(request, 'leaderboard/index.html', context)

def matchNumber(request):
	matches = [1]
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
	for user in users:
		name = str(user) + ' match#' + str(match)
		team = Team.objects.filter(name=name)
		ud = UserData.objects.get(user=user)
		if team.exists():
			team = team[0]
			for x in bat:
				team_player = PlayerTeam.objects.filter(team=team, player=x.player)
				if team_player.exists():
					ud.points += x.points
			for x in ball:
				team_player = PlayerTeam.objects.filter(team=team, player=x.player)
				if team_player.exists():
					ud.points += x.points
			for x in field:
				team_player = PlayerTeam.objects.filter(team=team, player=x.player)
				if team_player.exists():
					ud.points += x.points
			ud.save()
	return redirect('/leaderboard/')

