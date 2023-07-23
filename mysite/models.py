from django.db import models

class MainContent(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')