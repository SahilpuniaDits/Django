from django.contrib import admin
from django.urls import path
from .views import render_pdf_view,CustomerListView,customer_render_pdf_view

urlpatterns = [
    path('',CustomerListView.as_view(),name='customer-list-view'),
    path('test/',render_pdf_view,name='test-view'),
    path('pdf/<pk>/',customer_render_pdf_view,name='customer-pdf-view'),

]