from django.db import models
from players.models import Player

# Create your models here.
class Team(models.Model):
	name = models.CharField(max_length=40, primary_key=True, blank=True)
	black_mamba = models.ForeignKey(Player, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class PlayerTeam(models.Model):
	name = models.CharField(max_length=40, primary_key=True, blank=True)
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True)
	score = models.IntegerField(default=0)

	def __str__(self):
		return self.name