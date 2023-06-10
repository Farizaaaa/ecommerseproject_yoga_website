from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from ecommerce.models import category,product
from ecommerce.models import product


def ProDetail(request,c_slug,product_slug):
    try:
        products=product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render (request,'product.html',{'product':products})
# Create your views here.
# def index(request):
#     return HttpResponse("Hi")
def allProdCat(request,c_slug=None):
    c_page=None
    product_list=None
    if c_slug!=None:
        c_page=get_object_or_404(category,slug=c_slug)
        product_list=product.objects.all().filter(category=c_page,available=True)
    else:
        product_list=product.objects.all().filter(available=True)

    try:
            paginator = Paginator(product_list, 6)
            page=int(request.GET.get('page','1'))
            products = paginator.page(page)

    except (EmptyPage,InvalidPage):
            products=paginator.page(paginator.num_pages)
            page = 1
    return render(request,"category.html",{'category':c_page,'products':products})

