from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login ,logout
from django.http import JsonResponse  
import json
from django.http import HttpResponse
import random
from accounts.models import Accounts as User 
import urllib.request
import urllib.parse
import json
from claimzy_in import views


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
        mob = request.POST.get("mob")
        u = User.objects.get(mob=mob)
        if u is not None:
            n = random.randint(1000,9999) 
            message = 'Your OTP for User Login on ClaimZy is '+str(n)+'. Do not share this OTP to anyone.'
            u.set_password(str(n))
            u.save()
            otp(request,mob,message)
            print(n)
            request.session['_otp'] = n
            return HttpResponse("OTP Sent")
        else:
            return HttpResponse("Error!") 
    if not request.user.is_authenticated:
        return render(request,'users/login.html') 
    else:    
        return redirect('claimzy-home')    



def logout_view(request):
    logout(request)
    messages.success(request, f'You have successfully Logged out')
    return redirect('login')


                         
def sendSMS(apikey, numbers,  message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers, 'sender' : 'CLZYIN',
        'message' : message})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

def otp(request,number,message):
    #n = random.randint(1000,9999) 
    #'Claimzy OTP : '+str(n)
    resp =  sendSMS('9cnPqe+Y2bo-XUK0nJ6Eqv9DcYObVAe6dvr33H6fsV', number, message)
    data = json.loads(resp)
    s = json.dumps(data, indent=4, sort_keys=True)
    data = json.loads(s)
    
    print(data) 
    #print(n)
    #request.session['_otp'] = n 
    return render(request,'claimzy_in/admin/requests.html') 
 
def confirm_otp(request):   
    if request.session['_otp'] == int(request.POST.get('otp')):
          uname = request.POST.get("mob")
          password = request.POST.get("otp")  
          user = authenticate(username=uname,password=password)
          if user is not None :
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                    messages.success(request, f'Welcome {uname}')
                    return HttpResponse("")
                else:
                    messages.warning(request, f'Invalid Credentials')            
           
 