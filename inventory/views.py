from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, UpdateView

from inventory import forms
from inventory.models import Category


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
