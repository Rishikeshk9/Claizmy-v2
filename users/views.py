from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout

def register(request):
    if request.method == 'POST':
        uname = request.POST.get("uname")
        fname = request.POST.get("fname")           
        lname = request.POST.get("lname")           
        mail = request.POST.get("mail")
        password = request.POST.get("password")
        p = User.objects.create_user(username=uname, password=password, first_name=fname, last_name=lname, email=mail )
        p.save()
        messages.warning(request, f'{uname} Your Account has been created!')
        return redirect('login')

    return render(request,'users/register.html')


def log(request):
    if request.method == 'POST':
        uname = request.POST.get("mob")
        password = request.POST.get("otp")
        user = authenticate(mob=uname, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                messages.success(request, f'Welcome {uname}')
                return redirect('claimzy-home')
            else:
                messages.warning(request, f'Invalid Credentials')
  
    if not request.user.is_authenticated:
        return render(request,'users/login.html') 
    else:    
        return redirect('claimzy-home')    



def logout_view(request):
    logout(request)
    messages.success(request, f'You have successfully Logged out')
    return redirect('login')


   