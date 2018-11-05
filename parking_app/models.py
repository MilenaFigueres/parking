from django.db import models
from django.utils import timezone

class Own(models.Model):
	name = models.CharField(max_length=70)
	address = models.CharField(max_length=150, default='')
	location = models.CharField(max_length=150, default='')
	city = models.CharField(max_length=150, default='Mendoza')
	slack = models.CharField(max_length=150, default='')

	def __str__(self):
		return self.name


class Vehicle(models.Model):
	own = models.ForeignKey(
        Own,
        on_delete=models.CASCADE
    )
	patent = models.CharField(max_length=10)
	created_date = models.DateTimeField(
            default=timezone.now)
	color = models.CharField(max_length=50, default='')
	model = models.CharField(max_length=150, default='')

	def __str__(self):
		return self.patent


