from django.db import models

class Orders(models.Model):
    company = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    ram = models.IntegerField()
    rom = models.IntegerField()
    processor = models.CharField(max_length=50)
    price = models.FloatField()
    weight = models.FloatField()

# Create your models here.
