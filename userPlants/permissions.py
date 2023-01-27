from rest_framework import permissions
from users.models import User
from rest_framework.views import View
from .models import UserPlant


class IsPlantOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        pk = view.__dict__["kwargs"]["pk"]
        userPlant = UserPlant.objects.get(pk=pk)
        return request.user.is_authenticated and userPlant.userId == request.user
