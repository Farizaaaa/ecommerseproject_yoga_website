from django.shortcuts import render

# Create your views here.
from django.db.models import Q

from ecommerce.models import product


def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=product.objects.all().filter(Q(name__contains=query)|Q(description__contains=query))
        return render(request,'search.html',{'query':query,'products':products})