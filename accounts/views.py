from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm

def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "SIGNUP SUCCESS!")
            return redirect("/")
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html',{
        'form' : form,
    })
