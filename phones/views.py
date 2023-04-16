from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    if sort == 'name':
        products = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        products = Phone.objects.all().order_by('price')
    elif sort =='max_price':
        products = Phone.objects.all().order_by('-price')
    context = {'phones': products}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.filter(slug=slug).first()}
    return render(request, template, context)
