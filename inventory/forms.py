from django import forms

from inventory.models import Category, Product, Order


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer_name', 'customer_phone', 'customer_email', 'customer_address', 'product', 'qty')
