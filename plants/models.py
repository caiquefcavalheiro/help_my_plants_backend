from django.db import models

class Limit(models.Model):
    id = models.AutoField(primary_key=True)
    max = models.IntegerField()
    min = models.IntegerField()

class Plant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    cientific_name = models.CharField(max_length=50)
    water = models.IntegerField()
    temperature = models.OneToOneField("Limit", on_delete=models.CASCADE, related_name="plant_temperature")
    height = models.OneToOneField("Limit", on_delete=models.CASCADE, related_name="plant_height")
    lighting = models.OneToOneField("Limit", on_delete=models.CASCADE, related_name="plant_lighting")
    info = models.TextField(max_length=500)
    image = models.CharField(max_length=200)
