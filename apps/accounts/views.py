from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('core:home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Email yoki parol noto\'g\'ri'})

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('core:home')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')