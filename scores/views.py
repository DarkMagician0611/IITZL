from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from django.views.generic import ListView
from .models import BatRecord, BallRecord, FieldRecord, PlayedRecord
from players.models import Player
from django.urls import reverse_lazy
# Create your views here.

def index(request):
	return render(request, 'scores/index.html', {})

class BatList(ListView):
	queryset = BatRecord.objects.order_by('match', 'points').reverse()
	context_object_name = 'batrecord_list'

class BallList(ListView):
	queryset = BallRecord.objects.order_by('match', 'points').reverse()
	context_object_name = 'ballrecord_list'

class FieldList(ListView):
	queryset = FieldRecord.objects.order_by('match', 'points').reverse()
	context_object_name = 'fieldrecord_list'

class PlayedList(ListView):
	queryset = PlayedRecord.objects.order_by('match', 'points').reverse()
	context_object_name = 'playedrecord_list'

class BatDelete(DeleteView):
	model = BatRecord
	success_url = reverse_lazy('scores:batting')

class BallDelete(DeleteView):
	model = BallRecord
	success_url = reverse_lazy('scores:bowling')

class FieldDelete(DeleteView):
	model = FieldRecord
	success_url = reverse_lazy('scores:fielding')

class PlayDelete(DeleteView):
	model = PlayedRecord
	success_url = reverse_lazy('scores:playing')

def createBat(request):
	squads = ['Spartans', 'Musketeers', 'Redhawks', 'Thunder Strikers']
	return render(request, 'scores/addBat.html', {'squads' : squads})

def addBat(request):
	player = Player.objects.get(name=request.POST['player'])
	runs = int(request.POST['runs'])
	balls = int(request.POST['balls'])
	fours = int(request.POST['fours'])
	sixes = int(request.POST['sixes'])
	match = int(request.POST['match'])
	points = 2 * runs - balls + 2 * sixes + fours
	note = BatRecord(player=player, runs=runs, balls=balls, sixes=sixes, fours=fours, points=points, match=match)
	note.save()
	return redirect('/scores/batting/')

def createBall(request):
	squads = ['Spartans', 'Musketeers', 'Redhawks', 'Thunder Strikers']
	return render(request, 'scores/addBall.html', {'squads' : squads})

def addBall(request):
	player = Player.objects.get(name=request.POST['player'])
	runs = int(request.POST['runs'])
	balls = int(request.POST['balls'])
	wickets = int(request.POST['wickets'])
	match = int(request.POST['match'])
	wp = 0
	if wickets == 1:
		wp = 10
	elif wickets == 2:
		wp = 30
	elif wickets == 3:
		wp = 60
	elif wickets > 3:
		wp = 60 + (wickets - 3) * 30
	points = 7 * float(balls / 6) - runs + wp
	note = BallRecord(player=player, runs=runs, balls=balls, wickets=wickets, points=points, match=match)
	note.save()
	return redirect('/scores/bowling/')

def createField(request):
	squads = ['Spartans', 'Musketeers', 'Redhawks', 'Thunder Strikers']
	return render(request, 'scores/addField.html', {'squads' : squads})

def addField(request):
	player = Player.objects.get(name=request.POST['player'])
	stumps = int(request.POST['stumps'])
	catches = int(request.POST['catches'])
	run_outs = int(request.POST['run_outs'])
	match = int(request.POST['match'])
	points = 5 * stumps + 5 * catches + 5 * run_outs
	note = FieldRecord(player=player, stumps=stumps, catches=catches, run_outs=run_outs, points=points, match=match)
	note.save()
	return redirect('/scores/fielding/')

def createPlay(request):
	squads = ['Spartans', 'Musketeers', 'Redhawks', 'Thunder Strikers']
	return render(request, 'scores/addPlay.html', {'squads' : squads})

def addPlay(request):
	player = Player.objects.get(name=request.POST['player'])
	match = int(request.POST['match'])
	note = PlayedRecord(player=player, match=match)
	note.save()
	return redirect('/scores/playing/')

def loadPlayer(request):
	squad = request.GET.get('squad')
	players = Player.objects.filter(squad=squad)
	context = {'players' : players}
	return render(request, 'team/player_options.html', context)
