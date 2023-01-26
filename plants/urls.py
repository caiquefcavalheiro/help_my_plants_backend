from django.urls import path

from . import views

urlpatterns = [
    path("plants", views.PlantsView.as_view()),
    path("plants/<int:pk>", views.PlantViewId.as_view()),
]