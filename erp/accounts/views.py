from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm

def signup(request):
    if request.method == 'GET':
        form = SignupForm()
        return render(request, 'accounts/signup.html',{'form':form})
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            form = SignupForm()
            return render(request, 'accounts/signup.html', {'form':form, 'error':'잘못된 입력이 있습니다.'})
        

def user_login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'accounts/login.html',{'form':form})
    else:
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            form = LoginForm()
            return render(request, 'accounts/login.html', {'form':form, 'error':'잘못된 입력이 있습니다.'})


def user_logout(request):
    logout(request)
    return redirect('/login')