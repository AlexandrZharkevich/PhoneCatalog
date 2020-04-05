from django.http import HttpResponse
from django.shortcuts import render
from .models import Data


def index(request):
    return render(
        request,
        'index.html',
        {'data': Data.objects.order_by('reg_date')}
    )
