from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class BlogPost(models.Model):
    title = models.CharField( max_length=50)
    writer = models.CharField(max_length=50)
    thumbnail = models.ImageField( upload_to='images/')
    excerpt = models.CharField( max_length=150)
    content = models.TextField()
    featured = models.BooleanField(default = False)
    date_created = models.DateTimeField( default=datetime.now, blank=True)

    def __str__(self):
        return self.title

class Inquiry(models.Model):
    name = models.CharField( max_length=50)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    message = models.TextField()
    date_created = models.DateTimeField( default=datetime.now, blank=True)

    def __str__(self):
        return self.name