from django.contrib import admin
from django.db import models

# Create your models here.
class Expense(models.Model):
	date = models.DateField("Date")
	name = models.CharField(max_length=20)
	category = models.CharField(max_length=30)
	tax = models.FloatField(default = 0)
	tip = models.FloatField(default = 0)
	total = models.FloatField(default = 0)
	comments = models.CharField(max_length=100)

	class Meta:
		app_label = 'expenses'

	def __str__(self):
		return str(self.date) + " : " + str(self.name)
admin.site.register(Expense)

class Paycheck(models.Model):
	date = models.DateField("Date")
	name = models.CharField(max_length=20)
	tax = models.FloatField(default = 0)
	benefits = models.FloatField(default = 0)
	in_hand = models.FloatField(default = 0)
	total = models.FloatField(default = 0)
	comments = models.CharField(max_length=100)

	class Meta:
		app_label = 'expenses'

	def __str__(self):
		return str(self.date) + " : " + str(self.name)

admin.site.register(Paycheck)

class Bonus(models.Model):
	date = models.DateField("Date")
	name = models.CharField(max_length=20)
	in_hand = models.FloatField(default = 0)
	tax = models.FloatField(default = 0)
	total = models.FloatField(default = 0)
	comments = models.CharField(max_length=100)

	class Meta:
		app_label = 'expenses'

	def __str__(self):
		return str(self.date) + " : " + str(self.name)

admin.site.register(Bonus)