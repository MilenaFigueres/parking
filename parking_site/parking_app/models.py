from django.db import models
from django.utils import timezone

class Own(models.Model):
	name = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	address = models.CharField(max_length=150, default='')
	location = models.CharField(max_length=150, default='')
	city = models.CharField(max_length=150, default='')
	slack = models.CharField(max_length=150, default='')

	# def __string__(self):
 #        return self.name 


class Car(models.Model):
	own = models.ForeignKey(
        Own,
        on_delete=models.CASCADE
    )
	patent = models.CharField(max_length=10)
	created_date = models.DateTimeField(
            default=timezone.now)
	color = models.CharField(max_length=50, default='')
	model = models.CharField(max_length=150, default='')


