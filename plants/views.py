from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Plant
from .serializers import PlantSerializer
from plants.models import Limit


class PlantsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  

    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class PlantViewId(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  

    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
