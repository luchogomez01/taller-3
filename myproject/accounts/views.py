from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

# Vista para el login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('protected_view')  # Redirigir a la vista protegida si el login es exitoso
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

# Vista protegida (después del login)
@login_required
def protected_view(request):
    return render(request, 'protected.html')

# Vista para logout
def logout_view(request):
    auth_logout(request)
    return redirect('login')  # Redirige de nuevo al login después de cerrar sesión
