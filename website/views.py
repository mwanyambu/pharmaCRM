from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views import View 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin 
from django.contrib import messages 
from .forms import SignUpForm
from .forms import AddRecordForm
from .models import DoctorList
from .forms import SalesRepForm, MasterDoctorForm, DoctorVisitForm, VisitPlanForm, ProductForm, RegionForm, SupervisorReportForm
from .models import SalesRep, MasterDoctorList, DoctorVisit, VisitPlan, Product, Region, Supervisor
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

"""from .forms import DailyReportForm, AddRegionForm, AddProductForm, AddProductListForm"""
# Create your views here.
"""
class AdminCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser
class SalesRepCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and SalesRep.objects.filter(user=self.request.user).exists()
class SupervisorCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and Supervisor.objects.filter(user=self.request.user).exists()

"""
def login_page(request):
    return render(request, 'login.html')

# Decorator to require login for specific views
login_required_decorator = login_required(login_url='/login/')

def LandingPage(request):
    return render(request, 'LandingPage.html')

@method_decorator(staff_member_required, name='dispatch')
class SupervisorListView(ListView):
    model = Supervisor
    template_name = 'supervisor_list.html'

@method_decorator(staff_member_required, name='dispatch')
class SupervisorCreateView(CreateView):
    model = Supervisor
    template_name = 'supervisor_form.html'
    fields = ['user', 'sales_reps_assigned', 'phone', 'email']
    success_url = reverse_lazy('supervisor_list')

@method_decorator(staff_member_required, name='dispatch')
class SupervisorUpdateView(UpdateView):
    model = Supervisor
    template_name = 'supervisor_form.html'
    fields = ['user', 'sales_reps_assigned', 'phone', 'email']

@method_decorator(staff_member_required, name='dispatch')
class SupervisorDetailView(DetailView):
    model = Supervisor
    template_name = 'supervisor_detail.html'

@method_decorator(staff_member_required, name='dispatch')
class SupervisorDeleteView(DeleteView):
    model = Supervisor
    template_name = 'supervisor_confirm_delete.html'
    success_url = reverse_lazy('supervisor_list')

@method_decorator(login_required, name='dispatch')
class SalesRepListView(ListView):
    model = SalesRep
    template_name = 'salesrep_list.html'

@method_decorator(staff_member_required, name='dispatch')
class SalesRepCreateView(CreateView):
    model = SalesRep
    template_name = 'salesrep_form.html'
    fields = ['user', 'supervisor', 'region', 'phone', 'email']

@method_decorator(staff_member_required, name='dispatch')
class SalesRepUpdateView(UpdateView):
    model = SalesRep
    template_name = 'salesrep_form.html'
    fields = ['user', 'supervisor', 'region', 'phone', 'email']

@method_decorator(staff_member_required, name='dispatch')
class SalesRepDeleteView(DeleteView):
    model = SalesRep
    template_name = 'salesrep_confirm_delete.html'
    success_url = reverse_lazy('salesrep_list')

@method_decorator(login_required, name='dispatch')
class MasterDoctorListView(ListView):
    model = MasterDoctorList
    template_name = 'masterdoctorlist_list.html'

@method_decorator(staff_member_required, name='dispatch')
class MasterDoctorCreateView(CreateView):
    model = MasterDoctorList
    template_name = 'masterdoctorlist_form.html'
    fields = ['sales_rep', 'first_name', 'last_name', 'speciality', 'phone', 'Hospital_name', 'location']

@method_decorator(staff_member_required, name='dispatch')
class MasterDoctorUpdateView(UpdateView):
    model = MasterDoctorList
    template_name = 'masterdoctor_form.html'
    fields = ['sales_rep', 'first_name', 'last_name', 'speciality', 'phone', 'Hospital_name', 'location']

@method_decorator(staff_member_required, name='dispatch')
class MasterDoctorDeleteView(DeleteView):
    model = MasterDoctorList
    template_name = 'masterdoctor_confirm_delete.html'
    success_url = reverse_lazy('masterdoctor_list')

@method_decorator(login_required, name='dispatch')
class DoctorVisitListView(ListView):
    model = DoctorVisit
    template_name = 'doctorvisit_list.html'

@method_decorator(staff_member_required, name='dispatch')
class DoctorVisitCreateView(CreateView):
    model = DoctorVisit
    template_name = 'doctorvisit_form.html'
    fields = ['sales_rep', 'doctor', 'visit_date', 'visit_notes', 'feedback', 'status', 'supervisor']

@method_decorator(staff_member_required, name='dispatch')
class DoctorVisitUpdateView(UpdateView):
    model = DoctorVisit
    template_name = 'doctorvisit_form.html'
    fields = ['sales_rep', 'doctor', 'visit_date', 'visit_notes', 'feedback', 'status', 'supervisor']

@method_decorator(staff_member_required, name='dispatch')
class DoctorVisitDeleteView(DeleteView):
    model = DoctorVisit
    template_name = 'doctorvisit_confirm_delete.html'
    success_url = reverse_lazy('doctorvisit_list')

@method_decorator(staff_member_required, name='dispatch')
class RegionListView(ListView):
    model = Region
    template_name = 'region_list.html'

@method_decorator(staff_member_required, name='dispatch')
class RegionCreateView(CreateView):
    model = Region
    template_name = 'region_form.html'
    fields = ['region_name', 'assigned_rep']

@method_decorator(staff_member_required, name='dispatch')
class RegionUpdateView(UpdateView):
    model = Region
    template_name = 'region_form.html'
    fields = ['region_name', 'assigned_rep']

@method_decorator(staff_member_required, name='dispatch')
class RegionDeleteView(DeleteView):
    model = Region
    template_name = 'region_confirm_delete.html'
    success_url = reverse_lazy('region_list')

@method_decorator(staff_member_required, name='dispatch')
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

@method_decorator(staff_member_required, name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['product_name', 'product_description', 'product_price', 'product_quantity', 'product_category']

@method_decorator(staff_member_required, name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['product_name', 'product_description', 'product_price', 'product_quantity', 'product_category']

@method_decorator(staff_member_required, name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


@method_decorator(login_required, name='dispatch')
class VisitPlanListView(ListView):
    model = VisitPlan
    template_name = 'visitplan_list.html'

@method_decorator(staff_member_required, name='dispatch')
class VisitPlanCreateView(CreateView):
    model = VisitPlan
    template_name = 'visitplan_form.html'
    fields = ['sales_rep', 'doctor', 'visit_date', 'visit_notes', 'feedback']

@method_decorator(staff_member_required, name='dispatch')
class VisitPlanUpdateView(UpdateView):
    model = VisitPlan
    template_name = 'visitplan_form.html'
    fields = ['sales_rep', 'doctor', 'visit_date', 'visit_notes', 'feedback']

@method_decorator(staff_member_required, name='dispatch')
class VisitPlanDeleteView(DeleteView):
    model = VisitPlan
    template_name = 'visitplan_confirm_delete.html'
    success_url = reverse_lazy('visitplan_list')

def home(request):
    """
    Renders the home page and handles user login and registration.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    master_list = DoctorList.objects.all()
    # check if logged in
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # authenticate user
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login user
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Error logging in - please try again')
            return redirect('home')
    elif 'register' in request.POST:
        return register_user(request)
    else:
        return render(request, 'home.html', {'master_list':master_list})


def logout_user(request):
    """
    Logs out the user and redirects to the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

from django.contrib.auth import login

def register_user(request):
    """
    Handles user registration.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Create a SalesRep instance associated with the registered user
            sales_rep = SalesRep.objects.create(user=user, region='', phone='123456789', email=user.email)
            
            # Log in the user
            login(request, user)
            
            messages.success(request, 'You have been registered')
            return redirect('home')
        else:
            messages.error(request, 'Error registering - please try again')

    else:
        form = SignUpForm()
        print(form.errors)

    return render(request, 'register.html', {'form': form})

