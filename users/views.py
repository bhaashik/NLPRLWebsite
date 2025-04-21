from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
# from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login,authenticate
from .forms import UserRegistrationForm,UserLoginForm
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           user.is_active = False
           user.save()
           messages.success(request, f"Hello <b>{user.first_name}</b>! An account with <b> {user.email}</b> has been created.")
           return redirect('index')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})




def custom_login(request):
    
    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                email=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                # if user.is_active:
                login(request, user)
                messages.success(request, f"Hello <b>{user.email}</b>! You have been logged in")
                return redirect('index')

        else:
             for key, error in list(form.errors.items()):
                 messages.error(request, error) 

    form = UserLoginForm()
    
    return render(
        request=request,
        template_name="users/login.html", 
        context={'form': form}
        )


