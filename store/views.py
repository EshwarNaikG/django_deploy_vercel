from django.shortcuts import render

# Create your views here.

def Home(request):
    context = {}
    return render(request, 'store/home.html', context)


def Login(request):
    context = {}
    return render(request, 'store/login.html', context)

def Store(request):
    context = {}
    return render(request, 'store/store.html', context)


def Cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def Checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)




def Main(request):
    context = {}
    return render(request, 'store/main.html', context)


def About(request):
    context = {}
    return render(request, 'store/about.html', context)