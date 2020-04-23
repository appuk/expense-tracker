from django.db import models

# Create your models here.


class Paycheck(models.Model):
	date = models.DateField("Date")
	name = models.CharField(max_length=20)
	tax = models.FloatField(default = 0)
	benefits = models.FloatField(default = 0)
	in_hand = models.FloatField(default = 0)
	total = models.FloatField(default = 0)
	comments = models.CharField(max_length=100)

	class Meta:
		app_label = 'paychecks'

	def __str__(self):
		return str(self.date) + " : " + str(self.name)

