from django.shortcuts import render_to_response
from .models import *

def index(request):
    item = TestModel.objects.all()
    return render_to_response('test_app/index.html', {'item': item})

def main_category(request):
    items = Categories.objects.filter(parent=None)
    return render_to_response('test_app/main_categories.html', {'items': items})

def main_category2(request):
    items = Category2.objects.all()
    cover = Cover2.objects.all()
    print(dir(cover[1]))
    return render_to_response('test_app/main_category2.html', {'items': items, 'cover': cover})