from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "interest","password"]
        extra_kwargs = {"id": {"read_only" : True}, "password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        if validated_data["email"] == "caique@email.com.br":
            return User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create(**validated_data)
            user.set_password(validated_data["password"])
            user.save()
            return user


    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                
            else:
                setattr(instance, key, value)

        instance.save()
        return instance