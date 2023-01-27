from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Plant
from .serializers import PlantSerializer


class PlantsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]  

    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class PlantViewId(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]  

    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
