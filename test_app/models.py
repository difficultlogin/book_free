from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from filebrowser.fields import FileBrowseField

class TestModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    desc = HTMLField(null=True, blank=True)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    slug2 = AutoSlugField(populate_from='name', null=True, blank=True)


class Categories(models.Model):
    name = models.CharField(max_length=200)
    description = HTMLField(null=True, blank=True)
    cover = FileBrowseField('Image', max_length=200, directory='/files/media/uploads')
    parent = models.ForeignKey('self', blank=True, null=True, default='')
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

