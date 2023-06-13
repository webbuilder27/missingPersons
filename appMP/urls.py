from django.urls import path
from .views import MissingPersonsTable

urlpatterns = {
    path("", MissingPersonsTable, name="index"),
}