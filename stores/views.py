from django.shortcuts import render
from django.http import Http404
from .models import Store


# Create your views here.

def home(request):
    return render(request, 'home.html')

def store_list(request):
    stores = Store.objects.all()
    return render(request, 'store_list.html', locals())

def store_detail(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except:
        raise Http404
    return render(request, 'store_detail.html', locals())
