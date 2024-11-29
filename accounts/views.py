from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm  
from .forms import LoginForm 
from django.contrib.auth.forms import AuthenticationForm  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# View for Login Page
def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)      
        if form.is_valid():
          
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log the user in
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')  # Redirect to the homepage after login
            else:
                messages.error(request, 'Invalid credentials, please try again.')
        else:
            print(form.errors) 
            messages.error(request, 'Invalid form submission.')
    else:
        form = LoginForm()  # Create an empty form

    return render(request, 'accounts/login.html', {'form': form})

def register_page(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user}')
            return redirect('login_page')
        else:
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'accounts/register.html', context)
    return render(request, 'accounts/register.html', {})

def custom_logout_view(request):
    logout(request)
    return redirect('login_page')