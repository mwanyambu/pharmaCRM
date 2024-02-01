from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from .forms import SignUpForm
from .models import DoctorList

# Create your views here.
def home(request):
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
            #except:
            #   messages.error(request, 'Error logging in - please try again')
            #  return redirect('home')
    elif 'register' in request.POST:
        return register_user(request)
    else:
        #messages.error(request, 'Error logging in - please try again')
        return render(request, 'home.html', {'master_list':master_list})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

def register_user(request):
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
    if request.user.is_authenticated:
        doctor_list = DoctorList.objects.get(id=pk)
        return render(request, 'doctor_list.html', {'doctor_list':doctor_list})
    else:
        messages.sucess(request, 'you must log in - please try again')
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        deleted_list = DoctorList.objects.get(id=pk)
        deleted_list.delete()
        messages.success(request, 'You have deleted the doctor from the list')
        return redirect('home')
    else:
        messages.success(request, 'You must log in - please try again')
        return redirect('home')
 
