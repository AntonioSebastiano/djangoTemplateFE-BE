from django.db import models
#from django.core.validators import MaxValueValidator, MinValueValidator

class Exercise(models.Model):

    def __str__(self):
        return f'{self.name}'

    title = models.fields.CharField(max_length=100)
