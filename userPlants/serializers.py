from rest_framework import serializers
from .models import UserPlant
from plants.serializers import PlantSerializer, LimitSerializer

class UserPlantSerializer(serializers.ModelSerializer):
    temparature = LimitSerializer()
    lighting = LimitSerializer()
    height = LimitSerializer()
    plant = PlantSerializer()

    class Meta:
        model = UserPlant
        fields = ["id","name","cientific_name","water",
       "info","image","reminder","surname","last_watering",
       "details", "userId"]