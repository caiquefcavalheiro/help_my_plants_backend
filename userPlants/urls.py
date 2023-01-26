from django.urls import path

from . import views

urlpatterns = [
    path("userPlants", views.UserPlantsView.as_view()),
    path("userPlants/<int:pk>", views.UserPlantsViewId.as_view()),
]