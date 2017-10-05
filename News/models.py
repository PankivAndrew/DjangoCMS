from django.db import models


class News(models.Model):
    DateOfNews = models.DateField(null=True)
    NameOfNews = models.CharField(max_length=2000)
    NewsID = models.CharField(max_length=100, primary_key=True)
    HasVideo = models.BooleanField()


class Videos(models.Model):
    Video = models.FileField(upload_to='News/Videos')
    NameOfVideo = models.CharField(max_length=300, null=False)
    VideoID = models.CharField(max_length=100, null=False)
    News = models.ForeignKey(News, on_delete=models.CASCADE, null=True)
