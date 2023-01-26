from rest_framework import serializers
from .models import Plant, Limit

class LimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Limit
        fields = ["max", "min"]
        extra_kwargs = {"id": {"read_only": True}}


class PlantSerializer(serializers.ModelSerializer):
    temperature = LimitSerializer()
    lighting = LimitSerializer()
    height = LimitSerializer()

    class Meta:
        model = Plant
        fields = ["id", "name", "cientific_name",
        "water", "temperature", "lighting", "height", "info", "image"]
        extra_kwargs = {"id": {"read_only": True}}

    def create(self, validated_data: dict):
        temperature = validated_data.get("temperature", False)
        lighting = validated_data.get("lighting", False)
        height = validated_data.get("height", False)

        temperature_model = Limit.objects.create(**temperature)
        lighting_model = Limit.objects.create(**lighting)
        height_model = Limit.objects.create(**height)

        validated_data.update({"temperature": temperature_model})
        validated_data.update({"lighting" : lighting_model})
        validated_data.update({"height" : height_model})

        return Plant.objects.create(**validated_data)


    def update(self, instance: Plant, validated_data: dict):
        if validated_data.get("temperature", False):
            temperature = dict(validated_data.pop("temperature"))
            instance.temperature.max = temperature["max"]
            instance.temperature.min = temperature["min"]
            instance.temperature.save()

        if validated_data.get("lighting", False):
            lighting = dict(validated_data.pop("lighting"))
            instance.lighting.max = lighting["max"]
            instance.lighting.min = lighting["min"]
            instance.lighting.save()

        if validated_data.get("height", False):
            height = dict(validated_data.pop("height"))
            instance.height.max = height["max"]
            instance.height.min = height["min"]
            instance.height.save()

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance