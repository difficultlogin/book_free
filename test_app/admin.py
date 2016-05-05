from django.contrib import admin
from .models import *

class CoverInline(admin.StackedInline):
    model = Cover2

class Category2Admin(admin.ModelAdmin):
    inlines = [CoverInline]

admin.site.register(TestModel)
admin.site.register(Categories)
admin.site.register(Category2, Category2Admin)
admin.site.register(Cover2)