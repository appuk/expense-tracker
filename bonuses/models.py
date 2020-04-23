from django.db import models

# Create your models here.
class Bonus(models.Model):
	date = models.DateField("Date")
	name = models.CharField(max_length=20)
	in_hand = models.FloatField(default = 0)
	tax = models.FloatField(default = 0)
	total = models.FloatField(default = 0)
	comments = models.CharField(max_length=100)

	class Meta:
		app_label = 'bonuses'

	def __str__(self):
		return str(self.date) + " : " + str(self.name)
