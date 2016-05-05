from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from filebrowser.fields import FileBrowseField
from mptt.models import MPTTModel, TreeForeignKey

class TestModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    desc = HTMLField(null=True, blank=True)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    slug2 = AutoSlugField(populate_from='name', null=True, blank=True)


class Categories(models.Model):
    name = models.CharField(max_length=200)
    description = HTMLField(null=True, blank=True)
    cover = FileBrowseField('Image', max_length=200, directory='/files/media/uploads', default='/files/assets/images/placeholder.jpg')
    parent = models.ForeignKey('self', blank=True, null=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/test/categories/%s' % self.slug

class Category2(MPTTModel):
    name = models.CharField(max_length=200)
    description = HTMLField(null=True, blank=True)
    cover = FileBrowseField('Image', max_length=200, directory='/files/media/uploads',
                            default='/files/assets/images/placeholder.jpg')
    # cover = models.ImageField(null=True, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    auto_slug = AutoSlugField(populate_from='name', unique=True)
    # cover2 = models.ForeignKey('Cover', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/test/category2/%s' % self.auto_slug

    def get_images(self):
        obj = Cover2.objects.filter(parent_id=self.id)
        result = []
        for x in obj:
            result.append(x.image.url)
        return result

class Cover2(models.Model):
    image = FileBrowseField('Image', max_length=200, directory='/files/media/uploads',
                            default='/files/assets/images/placeholder.jpg')
    parent = models.ForeignKey('Category2')