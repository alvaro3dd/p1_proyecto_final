from django.shortcuts import render,redirect

from .forms import ProductForm, CategoryForm ,BrandForm
from .models import Product, Category, Brand

from django.urls import reverse_lazy  ## Class Views
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView ## Class Views


# **** General index

def index(request):
    return render(request,'product/index.html')



# ******* PRODUCTS (Func)

# def product_list(request):
#     # query = Product.objects.all()
#     # context = {'object_list':query}
#     # return render(request,'product/product_list.html', context)
    
#     q = request.GET.get('q')
#     if q:
#         query = Product.objects.filter(name__icontains=q)
#     else:
#         query = Product.objects.all()
#     context = {'object_list': query}
#     return render(request, 'product/product_list.html', context)


# def product_create(request):
#     if request.method == 'GET':
#         form = ProductForm()

#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('productos:product_list')

#     return render(request, 'product/product_form.html', {'form': form})


# def product_detail(request, pk:int):
#     query = Product.objects.get(id = pk)
#     context = {'object':query}
#     return render(request, 'product/product_detail.html',context)


# def product_update(request, pk:int):
#     query = Product.objects.get(id=pk)
#     if request.method == 'GET':
#         form = ProductForm(instance=query)

#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=query)
#         if form.is_valid():
#             form.save()
#             return redirect('productos:product_list')

#     return render(request, 'product/product_form.html', {'form': form})

# def product_delete(request, pk: int):
#     query = Product.objects.get(id=pk)
#     if request.method == 'POST':
#         query.delete()
#         return redirect('productos:product_list')
#     return render(request, 'product/product_confirm_delete.html', {'object': query})


# ******* PRODUCTS (Class views)


class ProductList(ListView):
    model = Product
    template_name = 'product/product_list.html' ## Preguntar como arreglar
    # context_object_name = 'categorias'
    # queryset = Product.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = Product.objects.filter(name__icontains=q)
        return queryset 
    

class ProductCreate(CreateView):
    model = Product
    from_class = ProductForm
    success_url = reverse_lazy('productos:product_list')
    template_name = 'product/product_form.html' ## Preguntar como arreglar
    fields = '__all__' #['name', 'description', 'price'] 


class ProductDetail(DetailView):
    model = Product
    # context_object_name = 'object'
    template_name = 'product/product_detail.html' ## Preguntar como arreglar


class ProductUpdate(UpdateView):
    model = Product
    from_class = ProductForm
    # context_object_name = 'object'
    template_name = 'product/product_form.html' ## Preguntar como arreglar
    success_url = reverse_lazy('productos:product_list')
    fields = '__all__' #['name', 'description', 'price'] 

class ProductDelete(DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html' ## Preguntar como arreglar
    success_url = reverse_lazy('productos:product_list')




# ******* Category (Class views)

class CategoryList(ListView):
    model = Category
    template_name = 'product/category_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = Category.objects.filter(name__icontains=q)
        return queryset 

class CategoryCreate(CreateView):
    model = Category
    from_class = CategoryForm
    success_url = reverse_lazy('productos:category_list')
    template_name = 'product/category_form.html' ## Preguntar como arreglar
    fields = '__all__' #['name', 'description', 'price'] 


# ******* Brand (Class views)

class BrandList(ListView):
    model = Brand
    template_name = 'product/brand_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = Brand.objects.filter(name__icontains=q)
        return queryset 
    


class BrandCreate(CreateView):
    model = Brand
    from_class = BrandForm
    success_url = reverse_lazy('productos:brand_list')
    template_name = 'product/brand_form.html' ## Preguntar como arreglar
    fields = '__all__' #['name', 'description', 'price'] 