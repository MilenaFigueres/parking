from django.db import models
from django.utils import timezone

class Own(models.Model):
	name = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	address = models.CharField(max_length=150, default='')
	location = models.CharField(max_length=150, default='')
	city = models.CharField(max_length=150, default='')


class Car(models.Model):
	own = models.ForeignKey(
        Own,
        on_delete=models.CASCADE
    )
	patent = models.CharField(max_length=10)
	color = models.CharField(max_length=50, default='')
	model = models.CharField(max_length=150, default='')


