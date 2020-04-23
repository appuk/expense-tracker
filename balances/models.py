from django.db import models

# Create your models here.
class Balance(models.Model):
	month = models.CharField(max_length=20)
	bofa1 = models.FloatField(default = 0)
	bofa2 = models.FloatField(default = 0)
	pnc = models.FloatField(default = 0)
	dcu = models.FloatField(default = 0)	
	fidelity = models.FloatField(default = 0)
	coastal = models.FloatField(default = 0)
	total = models.FloatField(default = 0)
	comments = models.CharField(max_length=100)

	class Meta:
		app_label = 'balances'

	def __str__(self):
		return str(self.month)
