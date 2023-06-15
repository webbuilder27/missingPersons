from django.urls import path
from .views import MissingPersonsTable, personView

urlpatterns = [
    # path('', homeView, name="homePage"),
    path("", MissingPersonsTable, name="index"),
    path('person/<str:personId>', personView, name="personView"),
]