from django.db import models
from players.models import Player
# Create your models here.
class BatRecord(models.Model):
	player = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)
	runs = models.IntegerField(default=0)
	balls = models.IntegerField(default=0)
	fours = models.IntegerField(default=0)
	sixes = models.IntegerField(default=0)
	points = models.FloatField(default=0)
	match = models.IntegerField(default=0)

	def __str__(self):
		return self.player.name + ' Batsman ' + str(self.points)

class BallRecord(models.Model):
	player = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)
	balls = models.IntegerField(default=0)
	runs = models.IntegerField(default=0)
	wickets = models.IntegerField(default=0)
	points = models.FloatField(default=0)
	match = models.IntegerField(default=0)

	def __str__(self):
		return self.player.name + ' Bowler ' + str(self.points)

class FieldRecord(models.Model):
	player = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)
	catches = models.IntegerField(default=0)
	stumps = models.IntegerField(default=0)
	run_outs = models.IntegerField(default=0)
	points = models.FloatField(default=0)
	match = models.IntegerField(default=0)

	def __str__(self):
		return self.player.name + ' Fielder ' + str(self.points)

class PlayedRecord(models.Model):
	player = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)
	match = models.IntegerField(default=0)
	points = models.IntegerField(default=2)

	def __str__(self):
		return self.player.name + ' Played ' + str(self.points)