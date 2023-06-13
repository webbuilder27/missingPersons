from django.db import models

# Create your models here.
class MissingPerson(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age_at_missing = models.PositiveIntegerField()
    city_of_disappearance = models.CharField(max_length=100)
    state_of_disappearance = models.CharField(max_length=100)
    date_of_disappearance = models.DateField()

    
    def __str__(self):
        return self.name