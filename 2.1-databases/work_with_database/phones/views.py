from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_catalog = request.GET.get('sort')
    ph_all = Phone.objects.all()
    if sort_catalog == 'low':
        ph_all = ph_all.order_by('price')
    elif sort_catalog == 'high':
        ph_all = ph_all.order_by('-price')
    elif sort_catalog == 'abc':
        ph_all = ph_all.order_by('name')

    context = {'phones': ph_all}
    return render(request, template, context)




def show_product(request, slug):
    template = 'product.html'
    product = Phone.objects.filter(slug=slug)
    context = {'phone': product}
    return render(request, template, context)
