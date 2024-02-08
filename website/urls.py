from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>/', views.doctor_list, name='doctor_list'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>/', views.update_record, name='update_record'),
    path('daily_report/', views.daily_report, name='daily_report'),
    path('add_product/', views.product_form, name='product_form'),
    path('product_list/', views.product_list, name='product_list'),
    path('region_list/', views.regions, name='regions'),
]

"""
URL patterns for the website.

This module defines the URL patterns for the PharmaCRM website. Each URL pattern is associated with a specific view function.

- The empty path ('') corresponds to the home view.
- The 'logout/' path corresponds to the logout_user view.
- The 'register/' path corresponds to the register_user view.
- The 'record/<int:pk>/' path corresponds to the doctor_list view, where <int:pk> is the primary key of a record.
- The 'delete_record/<int:pk>' path corresponds to the delete_record view, where <int:pk> is the primary key of a record.
- The 'add_record/' path corresponds to the add_record view.
- The 'update_record/<int:pk>/' path corresponds to the update_record view, where <int:pk> is the primary key of a record.
"""
