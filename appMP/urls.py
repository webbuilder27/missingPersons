from django.urls import path
from .views import MissingPersonsTable, personView
#This is listed in a specific order
#The first route takes you to the table
#The second route takes you to a separate page containing missing persons data. 
urlpatterns = [
    # path('', homeView, name="homePage"),
    path("", MissingPersonsTable, name="index"),
    path('person/<str:personId>', personView, name="personView"),
]