from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from .forms import SignUpForm
from .forms import AddRecordForm
from .models import DoctorList
from .forms import AddRecordForm
from .forms import DailyReportForm, AddRegionForm, AddProductForm, AddProductListForm
# Create your views here.

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
            # get username and password
            #username = form.cleaned_data['username']
            #password = form.cleaned_data['password1']
            # authenticate user
            #user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have been registered'))
            return redirect('home')
        else:
            messages.error(request, 'Error registering - please try again')
            #return redirect('register')
    else:
        form = SignUpForm()
        #return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def doctor_list(request, pk):
    """
    Renders the doctor list page for a specific doctor.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the doctor.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.user.is_authenticated:
        doctor_list = DoctorList.objects.get(id=pk)
        return render(request, 'doctor_list.html', {'doctor_list':doctor_list})
    else:
        messages.sucess(request, 'you must log in - please try again')
        return redirect('home')
    
def delete_record(request, pk):
    """
    Deletes a doctor record from the list.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the doctor record.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.user.is_authenticated:
        deleted_list = DoctorList.objects.get(id=pk)
        deleted_list.delete()
        messages.success(request, 'You have deleted the doctor from the list')
        return redirect('home')
    else:
        messages.success(request, 'You must log in - please try again')
        return redirect('home')

def add_record(request):
    """
    Adds a new doctor record to the list.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'You have added a doctor to the list')
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, 'You must log in - please try again')
        return redirect('home')
    
def update_record(request, pk):
    """
    Updates a doctor record in the list.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the doctor record.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.user.is_authenticated:
        doctor_list = DoctorList.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=doctor_list)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have updated the doctor list')
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, 'You must log in - please try again')
        return redirect('home')

def daily_report(request):
    """
    Adds a daily call report for a doctor.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    form = DailyReportForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                daily_report = form.save()
                messages.success(request, 'You have added a daily call report')
                return redirect('home')
        return render(request, 'daily_report.html', {'form':form})
    else:
        messages.success(request, 'You must log in - please try again')
        return redirect('home')
 
def product_form(request):
    """
    Adds a product record to the list.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    form = AddProductForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                product = form.save()
                messages.success(request, 'You have added a product to the list')
                return redirect('home')
        return render(request, 'product_form.html', {'form':form})
    else:
        messages.success(request, 'You must log in - please try again')
        return redirect('home')
    
 
def product_list(request):
    """
    Adds a product list record to the list.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    form = AddProductListForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                product_list = form.save()
                messages.success(request, 'You have added a product list to the list')
                return redirect('home')
        return render(request, 'product_list_form.html', {'form':form})
    else:
        messages.success(request, 'You must log in - please try again')
        return redirect('home')
    
def regions(request):
    """
    Adds a region record to the list.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    form = AddRegionForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                region = form.save()
                messages.success(request, 'You have added a region to the list')
                return redirect('home')
        return render(request, 'region_form.html', {'form':form})
    else:
        messages.success(request, 'You must log in - please try again')
        return redirect('home')
    
