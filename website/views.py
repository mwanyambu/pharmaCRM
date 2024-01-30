from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from . forms import SignUpForm

# Create your views here.
def home(request):
    # check if logged in
    if request.method == 'POST':
        username = request.POST['username', '']
        password = request.POST['password', '']
        # authenticate user
        if username and password:
            try:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    # login user
                    login(request, user)
                    messages.success(request, 'You have been logged in!')
                    return redirect('home')
                else:
                    messages.success(request, 'Error logging in - please try again')
                    return redirect('home')
            except:
                messages.success(request, 'Error logging in - please try again')
                return redirect('home')
    else:
        messages.error(request, 'Error logging in - please try again')
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # get username and password
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # authenticate user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have been registered'))
            return redirect('home')
        else:
            messages.error(request, 'Error registering - please try again')
            return redirect('register')
    else:
        form = SignUpForm()
        #return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})