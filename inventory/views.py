from _decimal import Decimal

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView

from inventory import forms
from inventory.models import Category, Product, Order


# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'


class AddCategoryView(CreateView):
    form_class = forms.CategoryForm
    template_name = 'add_category.html'
    queryset = Category.objects.all()
    success_url = '/category/'


class CategoryListView(ListView):
    template_name = 'category_list.html'
    queryset = Category.objects.all()
    context_object_name = 'objects'


# class CategoryEditView(View):
#     def get(self, request, pk):
#         instance = Category.objects.get(pk=pk)
#         context = {
#             'category_id': pk,
#             'form': forms.CategoryForm(instance=instance)
#         }
#         return render(request, template_name='edit_category.html', context=context)
#
#     def post(self, request, pk):
#         instance = Category.objects.get(pk=pk)
#         form = forms.CategoryForm(instance=instance, data=request.POST)
#         if form.is_valid():
#             form.save()
#         context = {
#             'category_id': pk,
#             'form': forms.CategoryForm(instance=instance)
#         }
#         return render(request, template_name='edit_category.html', context=context)

class CategoryEditView(UpdateView):
    form_class = forms.CategoryForm
    template_name = 'edit_category.html'
    queryset = Category.objects.all()
    success_url = '/category/'
    pk_url_kwarg = 'pk'


class CategoryDeleteView(View):

    def get(self, request, pk):
        instance = Category.objects.get(pk=pk)
        instance.delete()
        return redirect('/category/')


class ProductListView(ListView):
    template_name = 'product_list.html'
    queryset = Product.objects.all()
    context_object_name = 'objects'


class AddProductView(CreateView):
    form_class = forms.ProductForm
    template_name = 'add_product.html'
    queryset = Product.objects.all()
    success_url = '/product/'


class CreateOrderView(View):

    def get(self, request):
        context = {
            'form': forms.OrderForm
        }
        return render(request, 'add_order.html', context=context)

    def post(self, request):
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            customer_name = form.data['customer_name']
            customer_phone = form.data['customer_phone']
            customer_email = form.data['customer_email']
            customer_address = form.data['customer_address']
            product_id = form.data['product']
            product = Product.objects.get(id=product_id)
            qty = form.data['qty']
            subtotal = Decimal(product.price) * Decimal(qty)
            vat = Decimal(subtotal / 100) * Decimal(15)
            total = subtotal + vat
            product.qty = product.qty - int(qty)
            product.save()
            order = Order.objects.create(
                product=product, qty=qty, subtotal=subtotal, vat=vat, total=total, customer_name=customer_name,
                customer_phone=customer_phone, customer_email=customer_email, customer_address=customer_address
            )
            order.save()
        context = {
            'form': forms.OrderForm
        }
        return render(request, 'add_order.html', context=context)


class OrderListView(ListView):
    template_name = 'order_list.html'
    queryset = Order.objects.all()
    context_object_name = 'objects'


class OrderDetailView(DetailView):
    template_name = 'order_details.html'
    queryset = Order.objects.all()
    context_object_name = 'object'
