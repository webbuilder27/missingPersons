from django.db import models

# Create your models here.
#This Model is the background criteria that will be enforced when inputing data into the missing persons table via admin page. 
class MissingPerson(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age_at_missing = models.PositiveIntegerField()
    city_of_disappearance = models.CharField(max_length=100)
    state_of_disappearance = models.CharField(max_length=2)
    date_of_disappearance = models.DateField(default="YYYY-MM-DD")
    race = models.CharField(max_length=1)
    gender = models.CharField(max_length=1)
    
    # def __str__(self):
    #     return self.name
