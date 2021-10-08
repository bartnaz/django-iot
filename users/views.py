from django.shortcuts import render
from .forms import MySignUpForm

# Create your views here.



def register(request):

    if request.method == "POST":
        form = MySignUpForm(request.POST)
        if form.is_valid():
            user = form.save()


    form = MySignUpForm()
    return render(
        request=request,
        template_name='users/register.html',
        context = {
            'form': form
        }
    )