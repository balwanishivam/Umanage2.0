from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404,HttpResponse
from .models import Stock
from .forms import StockForm

def index(request):
    print(request.user)
    if request.user.is_authenticated:
        products = Stock.objects.filter(account=request.user)
        context = {'products': products}
        print(products)
        return render(request, 'Inventory/index.html', context)
    return HttpResponse("<h1>User not logged in</h1>")


def details(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Stock, pk=pk,account=request.user)
        return render(request, 'Inventory/detail.html', {'product': product})
    return HttpResponse("<h1>User not logged in</h1>")


def addnew(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = StockForm(request.POST)
            print(dir(form))
            if form.is_valid():
                instance=form.save(commit=False)
                instance.account=request.user
                form.save(commit=True)
                return redirect('Inventory:index')
        return HttpResponse("<h1>User not logged in</h1>")
    else:
        form = StockForm()
    return render(request, 'Inventory/new.html', {'form': form})


def edit(request, pk):
    product = get_object_or_404(Stock, pk=pk,account=request.user)
    if request.method == "POST":
        if request.user.is_authenticated:
            form = StockForm(request.POST, instance=product)
            if form.is_valid():
                print(product)
                form.save(commit=True)
                return redirect('Inventory:index')
        return HttpResponse("<h1>User not logged in</h1>")
    else:
        form = StockForm(instance=product)
    return render(request, 'Inventory/edit.html', {'form': form})

#def delete(request,pk):
#def search(request,product):

