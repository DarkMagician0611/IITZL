from django.shortcuts import render, redirect
from .models import Team, PlayerTeam, UserMatch
from django.contrib.auth.models import User
from players.models import Player
from leaderboard.models import UserData
from django.http import HttpResponse
import time

# Create your views here.
initial_anti_venom = 1100
squad_length = 11
squad_list = ['Musketeers', 'Redhawks', 'Spartans', 'Thunder Strikers']
# dummy = []

def index(request):
	um = UserMatch(user=request.user, match=request.POST['match'])
	um.save()
	name = str(request.user) + ' match#' + um.match
	team = Team.objects.filter(name=name)
	if team.exists():
		team_players = PlayerTeam.objects.filter(team=team[0])
		if len(team_players) > squad_length:
			team.delete()
			return render(request, 'team/team_create.html', {})
		context = {'team_players' : team_players, 'team' : team[0]}
		return render(request, 'team/final_team.html', context)
	else:
		match = int(um.match) - 1
		while match > 0:
			name = str(request.user) + ' match#' + str(match)
			team = Team.objects.filter(name=name)
			if team.exists():
				break
			match -= 1
		if match == 0:
			return render(request, 'team/team_create.html', {})
		else:
			team = team[0]
			name = str(request.user) + ' match#' + um.match
			new_team = Team(name=name, black_mamba=team.black_mamba)
			new_team.save()
			team_players = PlayerTeam.objects.filter(team=team)
			for team_player in team_players:
				player = team_player.player
				name = str(new_team) + str(player)
				new_team_player = PlayerTeam(team=new_team, player=player, name=name)
				new_team_player.save()
			new_team_players = PlayerTeam.objects.filter(team=new_team)
			context = {'team_players' : new_team_players, 'team' : new_team}
			return render(request, 'team/final_team.html', context)

def selectMatch(request):
	u = UserData.objects.filter(user=request.user)
	if not u.exists():
		ud = UserData(user=request.user)
		ud.save()
	ud = UserData.objects.get(user=request.user)
	info = ud.substitutes
	return render(request, 'team/match.html', {'info' : info})

def teamAddIndex(request):
	squads = squad_list
	um = UserMatch.objects.get(user=request.user)
	name = str(request.user) + ' match#' + um.match
	team = Team.objects.filter(name=name)
	if team.exists():
		team.delete()
	team_players = PlayerTeam.objects.none()
	context = {'team_players' : team_players, 'squads' : squads, 'count' : squad_length, 'anti_venom' : initial_anti_venom}
	return render(request, 'team/building_team.html', context)

def addPlayerLater(request):
	um = UserMatch.objects.get(user=request.user)
	name = str(request.user) + ' match#' + um.match
	team = Team.objects.filter(name=name)
	team = team[0]
	team_players = PlayerTeam.objects.filter(team=team)
	if len(team_players) == squad_length:
		return render(request, 'team/final_team.html', {'team_players' : team_players, 'team' : team})
	count = len(team_players)
	venom = 0
	for tp in team_players:
		venom += tp.player.venom
	anti_venom = initial_anti_venom - venom
	squads = squad_list
	count = squad_length - count
	context = {'team_players' : team_players, 'team' : team, 'squads' : squads, 'count' : count, 'anti_venom' : anti_venom}
	return render(request, 'team/building_team.html', context)

def checkValidity(team_players, team):
	players = []
	for tp in team_players:
		players.append(tp.player)
	error = ''
	if sum(player.category == 'Batsman' for player in players) < 3:
		error = 'Less Number of Batsmen, '
	if sum(player.category == 'Bowler' for player in players) < 3:
		error += 'Less Number of Bowlers, '
	if sum(player.category == 'Wicket-Keeper' for player in players) < 1:
		error += 'No Wicket-Keeper, '
	if sum(player.category == 'All-Rounder' for player in players) < 1:
		error += 'No All-Rounder, '
	if sum(player.fresher_pg == 'Fresher' for player in players) < 2:
		error += 'Less Number of UG Freshers, '
	if sum(player.fresher_pg == 'PG' for player in players) < 1:
		error += 'No PG'
	return error

def playerAdd(request):
	um = UserMatch.objects.get(user=request.user)
	name = str(request.user) + ' match#' + um.match
	team = Team.objects.filter(name=name)
	if team.exists():
		team = team[0]
		player = Player.objects.get(pk=request.POST['player'])
		name = str(team) + str(player)
		team_player = PlayerTeam(team=team, player=player, name=name)
		team_player.save()
		team_players = PlayerTeam.objects.filter(team=team)
		count = len(team_players)
		venom = 0
		for tp in team_players:
			venom += tp.player.venom
		anti_venom = initial_anti_venom - venom
		if anti_venom < 0:
			team_player.delete()
			return HttpResponse('<h2>Too much venom</h2>')
		if count == squad_length:
			error = checkValidity(team_players, team)
			if error == '':
				return render(request, 'team/addBlackMamba.html', {'players' : team_players})
			else:
				team_player.delete()
				return HttpResponse('<h2>' + error + '</h2>')
		else:
			squads = squad_list
			count = squad_length - count
			context = {'team_players' : team_players, 'team' : team, 'squads' : squads, 'count' : count, 'anti_venom' : anti_venom}
			return render(request, 'team/building_team.html', context)
	else:
		player = Player.objects.get(pk=request.POST['player'])
		team = Team(name=name, black_mamba=player)
		team.save()
		name = str(team) + str(player)
		team_player = PlayerTeam(team=team, player=player, name=name)
		team_player.save()
		squads = squad_list
		count = squad_length - 1
		anti_venom = initial_anti_venom - player.venom
		team_players = PlayerTeam.objects.filter(team=team)
		context = {'team_players' : team_players, 'squads' : squads, 'count' : count, 'anti_venom' : anti_venom}
		return render(request, 'team/building_team.html', context)

def loadPlayer(request):
	squad = request.GET.get('squad')
	um = UserMatch.objects.get(user=request.user)
	name = str(request.user) + ' match#' + um.match
	team = Team.objects.filter(name=name)
	exclude = []
	if team.exists():
		players = list(PlayerTeam.objects.filter(team=team[0]))
		exclude = [player.player.name for player in players]
	players = Player.objects.filter(squad=squad).exclude(name__in=exclude).order_by('venom').reverse()
	context = {'players' : players}
	return render(request, 'team/player_options.html', context)

def addBlackMamba(request):
	player = Player.objects.get(pk=request.POST['player'])
	um = UserMatch.objects.get(user=request.user)
	name = str(request.user) + ' match#' + um.match
	team = Team.objects.filter(name=name)
	team = team[0]
	team.black_mamba = player
	team.save()
	return redirect('/team/')

def deleteTeamPlayer(request, name):
	um = UserMatch.objects.get(user=request.user)
	team_name = str(request.user) + ' match#' + um.match
	team = Team.objects.filter(name=team_name)
	player = Player.objects.get(name=name)
	team_player = PlayerTeam.objects.filter(team=team[0], player=player)
	team_player = team_player[0]
	if team_player.player.name == team[0].black_mamba.name:
		team[0].black_mamba = None
	team_player.delete()
	team_players = PlayerTeam.objects.filter(team=team[0])
	count = len(team_players)
	venom = 0
	for tp in team_players:
		venom += tp.player.venom
	anti_venom = initial_anti_venom - venom
	squads = squad_list
	count = squad_length - count
	context = {'team_players' : team_players, 'team' : team, 'squads' : squads, 'count' : count, 'anti_venom' : anti_venom}
	return render(request, 'team/building_team.html', context)

def updateMamba(request):
	um = UserMatch.objects.get(user=request.user)
	name = str(request.user) + ' match#' + um.match
	team = Team.objects.filter(name=name)
	team_players = PlayerTeam.objects.filter(team=team[0])
	return render(request, 'team/addBlackMamba.html', {'players' : team_players})

def update(request, name):
	um = UserMatch.objects.get(user=request.user)
	team_name = str(request.user) + ' match#' + um.match
	team = Team.objects.filter(name=team_name)
	player = Player.objects.get(name=name)
	team_player = PlayerTeam.objects.filter(team=team[0], player=player)
	team_player = team_player[0]
	um.player = str(team_player)
	um.save()
	squads = squad_list
	return render(request, 'team/update.html', {'squads' : squads})

def playerUpdate(request):
	um = UserMatch.objects.get(user=request.user)
	name = str(request.user) + ' match#' + um.match
	team = Team.objects.filter(name=name)
	team = team[0]
	player = Player.objects.get(pk=request.POST['player'])
	name = str(team) + str(player) 
	team_player = PlayerTeam(team=team, player=player, name=name)
	team_player.save()
	venom = 0
	p = PlayerTeam.objects.get(name=um.player)
	team_players = PlayerTeam.objects.filter(team=team).exclude(player=p.player)
	for tp in team_players:
		venom += tp.player.venom
	anti_venom = initial_anti_venom - venom
	if anti_venom < 0:
		team_player.delete()
		um.player = ''
		um.save()
		return HttpResponse('<h2>Too much venom</h2>')
	error = checkValidity(team_players, team)
	if error == '' or len(team_players) < squad_length:
		p.delete()
		um.player = ''
		um.save()
		if p.player.name == team.black_mamba.name:
			return render(request, 'team/addBlackMamba.html', {'players' : team_players})
		else:
			return render(request, 'team/final_team.html', {'team_players' : team_players, 'team' : team})
	else:
		team_player.delete()
		um.player = ''
		um.save()
		return HttpResponse('<h2>' + error + '</h2>')

def resetTeam(request):
	um = UserMatch.objects.get(user=request.user)
	name = str(request.user) + ' match#' + um.match
	team = Team.objects.filter(name=name)
	team = team[0]
	team_players = PlayerTeam.objects.filter(team=team)
	team_players.delete()
	team.delete()
	return render(request, 'team/team_create.html', {})

def listTeams(request):
	matches = ['1', '2', '3', '4', '5', '6']
	teams = []
	black_mambas = []
	for match in matches:
		name = str(request.user) + ' match#' + match
		team = Team.objects.filter(name=name)
		if not team.exists():
			continue
		team = team[0]
		black_mambas.append(team.black_mamba)
		team_players = PlayerTeam.objects.filter(team=team)
		x = []
		for team_player in team_players:
			x.append(team_player)
		teams.append(x)
	context = {'teams' : teams, 'black_mambas' : black_mambas}
	return render(request, 'team/team_lists.html', context)

def createTeams(request):
	matches = [3, 4, 5, 6]
	users = User.objects.filter(groups__name='Players')
	for match in matches:
		for user in users:
			name = str(user) + ' match#' + str(match)
			team = Team.objects.filter(name=name)
			if team.exists():
				continue
			else:
				x = match - 1
				while(x > 0):
					name = str(user) + ' match#' + str(x)
					team = Team.objects.filter(name=name)
					if team.exists():
						break
					x -= 1
				if x != 0:
					team = team[0]
					name = str(user) + ' match#' + str(match)
					new_team = Team(name=name, black_mamba=team.black_mamba)
					new_team.save()
					team_players = PlayerTeam.objects.filter(team=team)
					for team_player in team_players:
						player = team_player.player
						name = str(new_team) + str(player)
						new_team_player = PlayerTeam(team=new_team, player=player, name=name)
						new_team_player.save()
	return redirect('/team/')
