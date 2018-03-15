from django.db import models

# Create your models here.
class Player(models.Model):
	name = models.CharField(max_length=20, primary_key=True)
	ssn = models.CharField(max_length=20, blank=True)
	squad = models.CharField(max_length=20, blank=True)
	category = models.CharField(max_length=15, blank=True)
	venom = models.IntegerField(default=0)
	fresher_pg = models.CharField(max_length=10, blank=True)

	def __str__(self):
		return self.name

class PlayerStats(models.Model):
	player = models.OneToOneField(Player, on_delete=models.CASCADE)
	runs = models.IntegerField(default=0)
	matches = models.IntegerField(default=0)
	highest_run = models.IntegerField(default=0)
	balls = models.IntegerField(default=0)
	wickets = models.IntegerField(default=0)
	run_conceded = models.IntegerField(default=0)
	highest_wicket = models.IntegerField(default=0)

	def __str__(self):
		return self.player.name