from django.shortcuts import render,redirect
from .forms import ProductForm


from .models import Product


def index(request):
    return render(request,'product/index.html')



# ******* PRODUCTS

def product_list(request):
    # query = Product.objects.all()
    # context = {'object_list':query}
    # return render(request,'product/product_list.html', context)
    
    q = request.GET.get('q')
    if q:
        query = Product.objects.filter(name__icontains=q)
    else:
        query = Product.objects.all()
    context = {'object_list': query}
    return render(request, 'product/product_list.html', context)


def product_create(request):
    if request.method == 'GET':
        form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('productos:product_list')

    return render(request, 'product/product_form.html', {'form': form})


def product_detail(request, pk:int):
    query = Product.objects.get(id = pk)
    context = {'object':query}
    return render(request, 'product/product_detail.html',context)


def product_update(request, pk:int):
    query = Product.objects.get(id=pk)
    if request.method == 'GET':
        form = ProductForm(instance=query)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('productos:product_list')

    return render(request, 'product/product_form.html', {'form': form})

def product_delete(request, pk: int):
    query = Product.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('productos:product_list')
    return render(request, 'product/product_confirm_delete.html', {'object': query})
