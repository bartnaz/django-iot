from django.shortcuts import render, redirect
from .forms import MySignUpForm, UserLoginForm
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'users/home.html', {'title': 'Homepage'})


def register(request):

    if request.method == "POST":
        form = MySignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Hello')
            return redirect('user-home')
    else:
        form = MySignUpForm()

    form = MySignUpForm()
    return render(
        request=request,
        template_name='users/register.html',
        context={
            'form': form
        }
    )


def login(request):
    form = UserLoginForm(request.POST)

    return render(
        request=request,
        template_name='users/login.html',
        context={
            'form': form
        }
    )


def profile(request):
    return render(request, 'users/profile.html')
