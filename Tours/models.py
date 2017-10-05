from django.db import models


class TypeOfTour(models.Model):
    NameOfTour = models.CharField(max_length=100, null=True)
    TypeOfTourID = models.CharField(primary_key=True, max_length=100)


class Tour(models.Model):
    NameOfTour = models.CharField(max_length=2000, null=True)
    DateOfTour = models.DateField(null=True)
    PriceOfTour = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    IsScheduled = models.NullBooleanField(null=True)
    TimeOfStarting = models.TimeField(null=True)
    Description = models.TextField(null=True)
    TourID = models.CharField(primary_key=True, max_length=100)
    TypeOfTour = models.ForeignKey(TypeOfTour, on_delete=models.CASCADE, null=True)


class Images(models.Model):
    NameOfImage = models.CharField(max_length=100, null=False)
    ImagesID = models.CharField(max_length=100, null=True)
    TourImage = models.ImageField(null=True, upload_to='Tours/Images')
    Tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=True)



