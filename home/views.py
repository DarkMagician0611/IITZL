from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	context = {}
	return render(request, 'home/index.html', context)

def admin(request):
	return redirect('/admin/')

def players(request):
	return redirect('/players/')

def team(request):
	return redirect('/team/')

def scores(request):
	return redirect('/scores/')

def leaderboard(request):
	return redirect('/leaderboard/')

def rules(request):
	return render(request, 'home/rules.html', {})