from django.shortcuts import render_to_response
from .models import *

def index(request):
    item = TestModel.objects.all()
    return render_to_response('test_app/index.html', {'item': item})