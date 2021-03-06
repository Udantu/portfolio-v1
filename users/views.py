from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm

def index(request):
    return render(request,"users/index.html")

def dashboard(request):
    return render(request,"users/dashboard.html")

def about(request):
    return render(request,"users/about.html")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, you are now able to login')
            return redirect('toLogin')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
