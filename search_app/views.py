from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
from django.core.paginator import Paginator


def searchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search_app/search.html', {'query': query, 'products': products})


def search(request):
    templates = 'search_app/search.html'
    query = request.GET.get('q')
    result = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    pages = Paginator(request, result)