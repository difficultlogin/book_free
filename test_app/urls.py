from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^categories/$', main_category),
    url(r'^category2/$', main_category2)
]