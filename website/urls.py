from django.urls import path
from . import views

from .views import SupervisorListView, SupervisorCreateView, SupervisorUpdateView, SupervisorDetailView, SupervisorDeleteView
from .views import SalesRepListView, SalesRepCreateView, SalesRepUpdateView, SalesRepDeleteView
from .views import MasterDoctorListView, MasterDoctorCreateView, MasterDoctorUpdateView, MasterDoctorDeleteView
from .views import DoctorVisitListView, DoctorVisitCreateView, DoctorVisitUpdateView, DoctorVisitDeleteView
from .views import RegionListView, RegionCreateView, RegionUpdateView, RegionDeleteView
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
from .views import VisitPlanListView, VisitPlanCreateView, VisitPlanUpdateView, VisitPlanDeleteView
from .views import LandingPage, login_page

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', login_page, name='login'),
    path('', LandingPage, name='landing_page'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    #path('record/<int:pk>/', views.doctor_list, name='doctor_list'),
    #path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    #path('add_record/', views.add_record, name='add_record'),
    #path('update_record/<int:pk>/', views.update_record, name='update_record'),
    #path('doctors/', views.doctors, name='doctors'),
    #path('sales_rep/', SalesRepView.as_view(), name='sales_rep'),
    #path('master_doctor/', MasterDoctorView.as_view(), name='master_doctor'),
    #path('doctor_visit/', DoctorVisitView.as_view(), name='doctor_visit'),
    #path('visit_plan/', VisitPlanView.as_view(), name='visit_plan'),
    #path('product/', ProductView.as_view(), name='product'),
    #path('region/', RegionView.as_view(), name='region'),
    #path('supervisor_reports/', SupervisorView.as_view(), name='supervisor_reports'),
    #path('doctors_data/', MasterDoctorView.as_view(), name='master_doctor_view'),
    #path('master-doctors/', views.display_master_doctors, name='display_master_doctors'),
    #path('master_doctor_form/', MasterDoctorFormView.as_view(), name='master_doctor_form'),
    path('supervisors/', SupervisorListView.as_view(), name='supervisor_list'),
    path('supervisors/create/', SupervisorCreateView.as_view(), name='supervisor_create'),
    path('supervisors/<int:pk>/', SupervisorDetailView.as_view(), name='supervisor_detail'),
    path('supervisors/<int:pk>/update/', SupervisorUpdateView.as_view(), name='supervisor_update'),
    path('supervisors/<int:pk>/delete/', SupervisorDeleteView.as_view(), name='supervisor_delete'),
    path('salesreps/', SalesRepListView.as_view(), name='salesrep_list'),
    path('salesreps/create/', SalesRepCreateView.as_view(), name='salesrep_create'),
    path('salesreps/<int:pk>/update/', SalesRepUpdateView.as_view(), name='salesrep_update'),
    path('salesreps/<int:pk>/delete/', SalesRepDeleteView.as_view(), name='salesrep_delete'),
    path('masterdoctors/', MasterDoctorListView.as_view(), name='masterdoctor_list'),
    path('masterdoctors/create/', MasterDoctorCreateView.as_view(), name='masterdoctor_create'),
    path('masterdoctors/<int:pk>/update/', MasterDoctorUpdateView.as_view(), name='masterdoctor_update'),
    path('masterdoctors/<int:pk>/delete/', MasterDoctorDeleteView.as_view(), name='masterdoctor_delete'),
    path('doctorvisits/', DoctorVisitListView.as_view(), name='doctorvisit_list'),
    path('doctorvisits/create/', DoctorVisitCreateView.as_view(), name='doctorvisit_create'),
    path('doctorvisits/<int:pk>/update/', DoctorVisitUpdateView.as_view(), name='doctorvisit_update'),
    path('doctorvisits/<int:pk>/delete/', DoctorVisitDeleteView.as_view(), name='doctorvisit_delete'),
    path('regions/', RegionListView.as_view(), name='region_list'),
    path('regions/create/', RegionCreateView.as_view(), name='region_create'),
    path('regions/<int:pk>/update/', RegionUpdateView.as_view(), name='region_update'),
    path('regions/<int:pk>/delete/', RegionDeleteView.as_view(), name='region_delete'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('visitplans/', VisitPlanListView.as_view(), name='visitplan_list'),
    path('visitplans/create/', VisitPlanCreateView.as_view(), name='visitplan_create'),
    path('visitplans/<int:pk>/update/', VisitPlanUpdateView.as_view(), name='visitplan_update'),
    path('visitplans/<int:pk>/delete/', VisitPlanDeleteView.as_view(), name='visitplan_delete'),
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
