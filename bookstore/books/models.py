from pyexpat import model
from django.db import models

# Import user model
from django.contrib.auth.models import User
# Import model validators
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(models.Model):
   
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) 
    year = models.PositiveIntegerField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.title


