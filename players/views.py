from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import Player
import pandas as pd

# Create your views here.
def playerList(request):
	musketeers = Player.objects.filter(squad='Musketeers').order_by('venom').reverse()
	redhawks = Player.objects.filter(squad='Redhawks').order_by('venom').reverse()
	spartans = Player.objects.filter(squad='Spartans').order_by('venom').reverse()
	thunder = Player.objects.filter(squad='Thunder Strikers').order_by('venom').reverse()
	context = {'musketeers' : musketeers, 'redhawks' : redhawks,
		'spartans' : spartans, 'thunder' : thunder}
	return render(request, 'players/player_list.html', context)

class PlayerDetail(generic.DetailView):
	model = Player
	template_name = 'players/player_detail.html'

def createPlayer(request):
	categories = ['Batsman', 'Bowler', 'All-Rounder', 'Wicket-Keeper']
	venoms = [25, 50, 100, 150, 200]
	freshers = ['Fresher', 'PG', 'None']
	squads = ['Spartans', 'Musketeers', 'Redhawks', 'Thunder Strikers']
	context = {'categories' : categories, 'venoms' : venoms, 'freshers' : freshers, 'squads' : squads}
	return render(request, 'players/player_create.html', context)

def addPlayer(request):
	name = request.POST['name']
	ssn = request.POST['ssn']
	squad = request.POST['squad']
	venom = int(request.POST['venom'])
	category = request.POST['category']
	freshers = request.POST['freshers']
	p = Player(name=name, ssn=ssn, squad=squad, venom=venom, category=category, fresher_pg=freshers)
	p.save()
	return redirect('/players/')

class PlayerDelete(DeleteView):
	model = Player
	success_url = reverse_lazy('players:player_list')

def autoAdd():
	df = pd.read_excel('IITZL.xlsx', 'Redhawks')
	name = df['Name']
	freshers = df['Freshers']
	category = df['Category']
	venom = df['Venom']

	for i in range(0, len(name)):
		p = Player(name=name[i], squad='Redhawks', venom=venom[i], category=category[i], fresher_pg=freshers[i])
		p.save()
