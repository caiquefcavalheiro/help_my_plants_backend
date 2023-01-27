from django.shortcuts import render
from rest_framework import generics
from .permissions import IsPlantOwner
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import UserPlant
from .serializers import UserPlantSerializer


class UserPlantsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  

    queryset = UserPlant.objects.all()
    serializer_class = UserPlantSerializer

    def get_queryset(self):
        userId = self.request.query_params.get("userId", None)
        
        if userId:
            return UserPlant.objects.filter(userId=userId)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(userId=user)



class UserPlantsViewId(generics.UpdateAPIView, generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsPlantOwner]

    queryset = UserPlant.objects.all()
    serializer_class = UserPlantSerializer
