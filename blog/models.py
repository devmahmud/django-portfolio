from django.db import models
from django.utils import timezone


class Post(models.Model):

    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField(default=timezone.now)
    image = models. ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title


class Quotes(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Quotes of the day"

    def __str__(self):
        return self.quote[:20]+"... -> "+self.author
