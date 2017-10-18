from django.db import models


# Create your models here.
class TourGuide(models.Model):
    Name = models.CharField(max_length=100, null=False)
    Image = models.ImageField(null=False, upload_to='TourGuide/Images')
    Description = models.TextField(null=False)
