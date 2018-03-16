from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def get_first_name(self):
    return self.first_name

User.add_to_class("__str__", get_first_name)

class UserData(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	points = models.FloatField(default=0)
	substitutes = models.IntegerField(default=20)

	def __str__(self):
		return str(self.user)