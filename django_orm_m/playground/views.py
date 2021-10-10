from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, OrderItem, Customer


def say_hello(request):
    '''query_set = Product.objects.filter(
        id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')'''

    query_set = Customer.objects.all()[0:5]

    return render(request, 'hello.html', {'name': 'Fahim', 'products': list(query_set)})
