from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product


def say_hello(request):
    query_set = Product.objects.order_by('-unit_price')

    return render(request, 'hello.html', {'name': 'Fahim', 'products': list(query_set)})
