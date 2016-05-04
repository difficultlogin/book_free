from django.db import models
from tinymce.models import HTMLField

class TestModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    desc = HTMLField(null=True, blank=True)
