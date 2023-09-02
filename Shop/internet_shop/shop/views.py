from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Item

def index(request):
    items = Item.objects.all()
    return render(request, 'shop/index.html', {'items': items})

def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'shop/item.html', {'item': item})

def buy(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    # Код для обработки покупки товара не готов
    return HttpResponseRedirect('/')
