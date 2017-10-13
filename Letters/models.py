from django.db import models


# Create your models here.

class Letter(models.Model):
    WhoSent = models.CharField(max_length=100, null=False)
    NameOfTour = models.CharField(max_length=200, null=False)
    AmountOfPeople = models.IntegerField(null=False)
    LanguageOfTour = models.CharField(max_length=100, null=False)
    DateOfTour = models.DateField(null=False)
    PhoneNumber = models.CharField(max_length=15, null=False)
    Email = models.EmailField(null=False)
