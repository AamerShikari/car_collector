from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Car(models.Model):
	make = models.CharField(max_length=100)
	model = models.CharField(max_length=250)
	year = models.DateField()
	color = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self)
        return f"The car {self.make} {self.model} has id of {self.id}"

    def get_absolute_url(self)
        return reverse('detail', kwargs={'car_id':self.id})