from django.urls import path

from . import views

urlpatterns = [
    path("userPlants", views.UserPlantsViewCreate.as_view()),
    path("userPlants/", views.UserPlantsViewList.as_view()),
    path("userPlants/<int:pk>", views.UserPlantsViewId.as_view()),
]