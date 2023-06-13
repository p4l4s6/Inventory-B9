from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('category/create/', views.AddCategoryView.as_view(), name='add-category'),
    path('category/', views.CategoryListView.as_view(), name='list-category'),
    path('category/edit/<int:pk>/', views.CategoryEditView.as_view(), name='edit-category'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete-category')
]
