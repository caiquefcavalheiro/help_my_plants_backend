from django.db import models

class UserPlant(models.Model):
    id = models.AutoField(primary_key=True)
    
    reminder = models.CharField(max_length=50,blank=True)
    surname = models.CharField(max_length=50,blank=True)
    last_watering = models.DateTimeField(null=True)
    details = models.CharField(max_length=50, blank=True)

    name = models.CharField(max_length=40)
    cientific_name = models.CharField(max_length=50)
    water = models.IntegerField()
    lighting = models.OneToOneField("plants.Limit", on_delete=models.CASCADE, related_name="userPlant_lighting")
    temperature = models.OneToOneField("plants.Limit", on_delete=models.CASCADE, related_name="userPlant_temperature")
    height = models.OneToOneField("plants.Limit", on_delete=models.CASCADE, related_name="userPlant_height")
    info = models.TextField(max_length=500)
    image = models.CharField(max_length=200)

    userId = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="userPlants")

    