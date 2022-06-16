from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def catalog(request):
    return render(request, 'pages/catalog.html')


def product_single(request, slug=None):
    return render(request, 'pages/single-product.html')
