from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import UserPlant
from .serializers import UserPlantSerializer


class UserPlantsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  

    queryset = UserPlant.objects.all()
    serializer_class = UserPlantSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(userId=user)


class UserPlantsViewId(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = UserPlant.objects.all()
    serializer_class = UserPlantSerializer