from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('category/create/', views.AddCategoryView.as_view(), name='add-category'),
    path('category/', views.CategoryListView.as_view(), name='list-category'),
    path('category/edit/<int:pk>/', views.CategoryEditView.as_view(), name='edit-category'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete-category'),

    path('product/', views.ProductListView.as_view(), name='list-product'),
    path('product/create/', views.AddProductView.as_view(), name='add-product'),

    path('order/', views.OrderListView.as_view(), name='list-order'),
    path('order/create/', views.CreateOrderView.as_view(), name='add-order'),

    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='detail-order'),
]
