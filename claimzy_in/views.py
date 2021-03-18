from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Claim,Devices
from accounts.models import Accounts as User
from django.contrib import messages
from django.http import JsonResponse
import urllib.request
import urllib.parse
import json
from django.core.files.storage import FileSystemStorage
import random
import razorpay
from django.views.decorators.csrf import csrf_exempt
import sqlite3 as sql
import os
import csv
from sqlite3 import Error
from django.conf import settings
from django.http import HttpResponse, Http404
from datetime import datetime



customers = User.objects.filter(is_customer="True")
vendors = User.objects.filter(is_vendor="True")

def claimzy(request):
     return render(request,'claimzy_in/client/index.html',{'User': User,})

def test(request):
     return render(request,'claimzy_in/client/test.html',{'User': User,})

def user_register(request):
     if request.method == 'POST':
          plan = request.POST.get("plan")
          brand = request.POST.get("brand")
          return render(request,'claimzy_in/client/register.html',{'Plan': plan,'Brand':brand})

@csrf_exempt
def verify(request):
     print("Verifying...")
     print(request.method)
     print(request.POST.get('razorpay_payment_id'))
     return

@csrf_exempt
def status(request):
     return render(request,'claimzy_in/client/status.html')

@csrf_exempt
def capture(request):
     if request.method == 'POST':

          keyid = "rzp_live_nIDSu6ZA7x9y5m" #Live
          #keyid = "rzp_test_D8prDPzKLWt8hZ" #Test
          
          keysecret = "pHyzwpJCJnQPtvCNGz7PSK9x" #Live
          #keysecret = "oCDib2hyOMhSnYhMAijFS9a3" #Test
          client = razorpay.Client(auth=(keyid, keysecret))
          payment_id = request.POST.get("paymentid")
          print(payment_id)
          payment_amount = request.POST.get("amt")
          print(payment_amount)
          mob = request.POST.get("mobile")
          print(mob)
          imei = request.POST.get("imei")
          payment_currency = "INR"
          resp = client.payment.fetch(payment_id)
          #resp = client.payment.capture(payment_id, payment_amount, {"currency":"payment_currency"})
          print("Received Request Status: ",resp['status'])
          if(resp['status']=="authorized"):
               message = 'Hi. '+str(mob)+' \nCongratulations! You have successfully registered for ClaimZy Extended Warranty. For more details visit www.claimzy.in'
               otp(request,mob,message)
          else:
               Devices.objects.filter(imei=imei).delete()
          return HttpResponse(resp['status'])

"""p = ''

def verify(request):
     if request.method == 'POST':
          p_id = request.POST.get('p_id')
          if p_id!=None:
               p.
"""

'''def verif(request):
   '''
@csrf_exempt
def upload_file(request):
    customers = User.objects.filter(is_customer="True")
    vendors = User.objects.filter(is_vendor="True")
    if request.method == 'POST':
       name = request.POST.get('name')
       mob = request.POST.get('mob')
       add = request.POST.get('address')
       add2 = request.POST.get('address2')
       city = request.POST.get('city')
       pincode = request.POST.get('pincode')
       state = request.POST.get('state')

       brand = request.POST.get('brand')
       model = request.POST.get('model')
       imei = request.POST.get('imei')
       price = request.POST.get('price')
       date = request.POST.get('date')
       plan = request.POST.get('plan')
     
       invoice_pic = request.FILES['invoice-pic']
        
       imei_pic = request.FILES['imei-img']
       front_pic = request.FILES['front']
       back_pic = request.FILES['back']
       fs = FileSystemStorage()
       '''path = default_storage.save("upload/uploads.jpg", request.FILES['file'])'''
       invoice      = fs.save('claimzy_in/userdata/invoice/'+invoice_pic.name, invoice_pic)
       imei_pic     = fs.save('claimzy_in/userdata/imei/'+imei_pic.name, imei_pic)
       front        = fs.save('claimzy_in/userdata/front/'+front_pic.name, front_pic)
       back         = fs.save('claimzy_in/userdata/back/'+back_pic.name, back_pic)
       vend_id = ""
       print(mob,name,add,add2,city,pincode,state)
       if request.user in customers:
          name = request.user.name
          mob = request.user.mob
          add = request.user.address  
          add2 = request.user.addresstwo  
          city = request.user.city  
          pincode = request.user.pincode  
          state = request.user.state  
          
       elif request.user in vendors:
          if request.user.is_authenticated:
             vend_id = request.user.id
             p = User.objects.create_user(name=name, mob=mob, address=add, addresstwo=add2, city=city, pincode=pincode, state=state) 
             p.save()

       else:
          p = User.objects.create_user(name=name, mob=mob, address=add, addresstwo=add2, city=city, pincode=pincode, state=state)
          p.save()

       print(add)
       
       if (int(price)<=40000 and int(price) > 20000):
            print("Gold")
            print(plan)
            if(plan=="gold"):  
                 Devices.objects.create(mob=User.objects.get(mob=mob),brand=brand,model=model,imei=imei,price=price,invoice_date=date,plan=plan,invoice=invoice,imei_pic=imei_pic,front=front,back=back,vend=vend_id)
                 print("Gold Plan, Object created")
               
       elif (int(price) >= 5000 and int(price) <=20000):
            print("Silver")
            print(plan)
            if(plan=="silver"):
                 Devices.objects.create(mob=User.objects.get(mob=mob),brand=brand,model=model,imei=imei,price=price,invoice_date=date,plan=plan,invoice=invoice,imei_pic=imei_pic,front=front,back=back,vend=vend_id)
                 print("Silver Plan, Object created")
       
       else:
            return HttpResponse("Invalid Plan")

       success = "Success! Please proceed to Payment"

       return HttpResponse(success)

       #return render(request,'claimzy_in/client/test.html' )
    return render(request,'claimzy_in/client/index.html' )

def home(request):
     customers = User.objects.filter(is_customer="True")
     vendors = User.objects.filter(is_vendor="True")
     if not request.user.is_authenticated:
          return redirect('login')
     else:
          is_customer=False

          if request.user in customers:
               is_customer=True
               device = Devices.objects.filter(mob=request.user,status='Approved')
               claims_obj = Claim.objects.filter(mob=request.user)
               return render(request,'claimzy_in/admin/tables.html',{'User': User,'Customer': is_customer,'Claims':claims_obj,'Devices': device})
          is_vendor=False
          if request.user in vendors:
               is_vendor=True
               device = Devices.objects.filter(mob=request.user)
               claims_obj = Claim.objects.filter(mob=request.user)
               return render(request,'claimzy_in/admin/dashboard.html',{'User': User,'Vendor': is_vendor,'Claims':claims_obj,'Devices': device})
          return render(request,'claimzy_in/admin/dashboard.html',{'User': User,'Customer': is_customer,'Vendor': is_vendor})

def users(request):
     customers = User.objects.filter(is_customer="True")
     vendors = User.objects.filter(is_vendor="True")

     is_customer=False
     if request.user in customers:
          is_customer=True

     device = vendors

     user1 = User.objects.filter(is_superuser=False,is_vendor=True)
     is_vendor=False
     if request.user in vendors:
               is_vendor=True
               device = Devices.objects.filter(vend=request.user.id)
#claims_obj = Claim.objects.filter(mob=request.user)
#return render(request,'claimzy_in/admin/tables.html',{'User': user,'Vendor': is_vendor,'Claims':claims_obj,'Devices': device})

     return render(request,'claimzy_in/admin/tables.html',{'User': user1,'Vend':vendors,'Cust': customers,'Customer': is_customer,'Vendor': is_vendor,'Devices': device })

def usersdetails(request):
     uid = 3
     if request.method == 'POST':
        uid = request.POST.get("id")
        uname = request.POST.get("uname")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        mail = request.POST.get("mail")
        user = User.objects.get(id=uid)
        user.username=uname
        user.first_name=fname
        user.last_name=lname
        user.email=mail
        messages.success(request, f'{uname} Your Account has been Updated!')
        return redirect('claimzy-usersdetails')

     return render(request,'claimzy_in/admin/user.html' )

def custdetails(request):
     uid = ""
    # user = User.objects.filter(id=current_user.id)
     if request.user.is_superuser:
          if request.method == 'GET':
               uid = request.GET.get("id")
               cust = User.objects.get(id=uid)
               print(uid)
               #messages.success(request, f'{uname} Your Account has been Updated!')
               print (cust.id)
               return render(request,'claimzy_in/admin/profile-customer.html',{'Cust':cust})
     return HttpResponse("ERROR 404")


def mydetails(request):
     customers = User.objects.filter(is_customer="True")
     vendors = User.objects.filter(is_vendor="True")
     is_customer=False
     current_user = request.user
     user = User.objects.filter(id=current_user.id)
     if request.user in customers:
          is_customer=True
          return render(request,'claimzy_in/admin/profile.html',{'User': User,'Customer': is_customer})
     is_vendor=False
     if request.user in vendors:
               is_vendor=True
               device = Devices.objects.filter(mob=request.user)
               claims_obj = Claim.objects.filter(mob=request.user)
               return render(request,'claimzy_in/admin/profile.html',{'User': User,'Vendor': is_vendor,'Claims':claims_obj,'Devices': device})

     return render(request,'claimzy_in/admin/profile.html',{'User': user,} )

def claims(request):
     context = {

     }
     return render(request,'claimzy_in/admin/claims.html',context)

def user_claims(request):
     customers = User.objects.filter(is_customer="True")
     vendors = User.objects.filter(is_vendor="True")
     is_customer=False
     claims_obj = Claim.objects.all()

     if request.user in customers:
          is_customer=True
          claims_obj = Claim.objects.filter(mob=request.user)
     is_vendor=False
     if request.user in vendors:
               is_vendor=True
               device = Devices.objects.filter(mob=request.user)
               claims_obj = Claim.objects.filter(mob=request.user)
               return render(request,'claimzy_in/admin/claims.html',{'User': User,'Vendor': is_vendor,'Claims':claims_obj,'Devices': device})

     return render(request,'claimzy_in/admin/claims.html',{'claims': claims_obj,'Customer': is_customer} )

def map(request):
     return render(request,'claimzy_in/admin/map.html')

def about(request):
     return HttpResponse('<h1>About</h1>')

def claim_status(request):
     id = request.GET.get('id')
     status = request.GET.get('status')
     today = datetime.now()

     d2 = today.strftime("%Y-%m-%d %H:%M:%S")
     print(d2)
     q = Claim.objects.filter(id=id).update(status=status,last_update=d2)
     claimObj = Claim.objects.get(id=id)
     mob = claimObj.mob
     print(claimObj.mob_id)
     message = 'Hello ' +str(claimObj.mob)+' \nYour current claim status is : '+str(status)+'; Check profile for further updates.'
     print (message)
     otp(request,claimObj.mob,message)
     if status=="Complete" or status=="Rejected" :
          dvc = Devices.objects.filter(id=claimObj.device_id).update(status="Approved")
                  
     return JsonResponse(q,safe=False)

def request_status(request):
     id = request.GET.get('id')
     today = datetime.now()

     d2 = today.strftime("%Y-%m-%d %H:%M:%S")
     status = request.GET.get('status')
     q = Devices.objects.filter(id=id).update(status=status,last_update=d2)
     deviceObj = Devices.objects.get(id=id)
     message = 'Hello ' +str(deviceObj.mob)+' \nYour Device registration is '+str(status)+'; Check profile for further updates.'
     print (message)
     otp(request,deviceObj.mob,message)
     return JsonResponse(q,safe=False)

def updateprofile(request):
     customers = User.objects.filter(is_customer="True")
     vendors = User.objects.filter(is_vendor="True")
     if request.method == 'POST':
          uid = request.POST.get('id')
          name = request.POST.get('name')
          mob = request.POST.get('mob')
          add = request.POST.get('address')
          add2 = request.POST.get('address2')
          city = request.POST.get('city')
          pincode = request.POST.get('pincode')
          state = request.POST.get('state')
          print(uid)
          userprofile = User.objects.filter(id=uid).update(name=name,address=add,addresstwo=add2,city=city,pincode=pincode,state=state)
          print(request.user.id)
          if int(request.user.id) == int(uid):
               return redirect('claimzy-mydetails')
          else:
               return HttpResponseRedirect("http://127.0.0.1:8000/profile-customer?id="+str(uid))
     





def device_register(request):
     if(request.user_agent.is_mobile or request.user_agent.is_tablet or request.user_agent.is_touch_capable):
          print("else ran")
     else:
          print("it is a mobile or handheld")
          return HttpResponse("You cannot access this page.")
     customers = User.objects.filter(is_customer="True")
     vendors = User.objects.filter(is_vendor="True")
     is_customer=False
     if request.user in customers:
               is_customer=True
               device = Devices.objects.filter(mob=request.user)
               claims_obj = Claim.objects.filter(mob=request.user)
     is_vendor=False
     if request.user in vendors:
               is_vendor=True
               device = Devices.objects.filter(mob=request.user)
               claims_obj = Claim.objects.filter(mob=request.user)
               
     print(is_customer,is_vendor)
     return render(request,'claimzy_in/admin/device-register.html',{'Vend':vendors,'Cust': customers,'User': User,'Customer': is_customer,'Vendor': is_vendor,'Claims':claims_obj,'Devices': device}  )


def image_register(request):
     if(request.user_agent.is_mobile or request.user_agent.is_tablet or request.user_agent.is_touch_capable):
          print("else ran")
     else:
          print("it is a mobile or handheld device")
          return HttpResponse("You cannot access this site.")
     customers = User.objects.filter(is_customer="True")
     vendors = User.objects.filter(is_vendor="True")
     if request.method == 'POST':
          plan = request.POST.get("plan")
          name = request.POST.get("name")
          mob = request.POST.get("mobile")
          address = request.POST.get("address")
          address2 = request.POST.get("address2")
          city = request.POST.get("city")
          pincode = request.POST.get("pincode")
          state = request.POST.get("state")

          brand = request.POST.get("brand")
          model = request.POST.get("model")
          customers = User.objects.filter(is_customer="True")
          vendors = User.objects.filter(is_vendor="True")
          is_customer=False
          if request.user in customers:
               is_customer=True
               name = request.user.name
               mob = request.user.mob
               address = request.user.address
               address2 = request.user.addresstwo
               city = request.user.city
               pincode = request.user.pincode
               state = request.user.state

          is_vendor=False
          if request.user in vendors:
               is_vendor=True
          n = random.randint(1000,9999)
          print(n)
          request.session['_otp'] = n

          message = "Verification code for Claimzy : " +str(n)
          #Verification code for Claimzy : %%|otp^{"inputtype" : "text", "maxlength" : "5"}%%
          request.session['_otp'] = n
          otp(request,mob,message)
          return render(request,'claimzy_in/admin/image-register.html',{'plan':plan, 'name':name, 'mob':mob,'address':address,'address2':address2,'city':city,'pincode':pincode,'state':state, 'brand':brand, 'model':model, 'User': User,'Customer': is_customer,'Vendor': is_vendor,'isvendor':is_vendor,'iscustomer': is_customer} )

def requests(request):
     customers = User.objects.filter(is_customer="True")
     vendors = User.objects.filter(is_vendor="True")
     plan =''
     is_customer=False
     if request.user in customers:
               is_customer=True
               device = Devices.objects.filter(mob=request.user)
               claims_obj = Claim.objects.filter(mob=request.user)
     is_vendor=False
     device = Devices.objects.filter(status="Under Review")
     cust_name=[]
     id_list = []
     if request.user in vendors:
               is_vendor=True
               device = Devices.objects.filter(mob=request.user)
               claims_obj = Claim.objects.filter(mob=request.user)
               return render(request,'claimzy_in/admin/image-register.html',{'User': User,'Vendor': is_vendor,'Claims':claims_obj,'Devices': device})
 
     for deviceObj in device:

          cust =     User.objects.get(mob=deviceObj.mob)
          cust_name.append(cust.name)
          id_list.append(cust.id)
      
     #print(cust_name[0])
     if request.method == 'POST':
          plan = request.POST.get("plan")
          #print (device.mob)
     return render(request,'claimzy_in/admin/requests.html',{'Plan':plan,'User': User,'Customer': is_customer,'Devices': device,'CustomerList':cust_name,'CustomerID':id_list} )

def devices(request):
     device = Devices.objects.filter(status="Approved")
     return render(request,'claimzy_in/admin/devices.html',{ 'User': User, 'Devices': device} )

def vendors(request):
     vendors = User.objects.filter(is_vendor=True)
     return render(request,'claimzy_in/admin/vendor-table.html',{ 'Vendor': vendors } )

def download_report(request):
      # Export data into CSV file
        # Connect to database
     conn=sql.connect('db.sqlite3')
     print("Exporting data into CSV............")
     cursor = conn.cursor()
     cursor.execute("select * from accounts_accounts")
     path = "claimzy-accounts_report.csv" 
     
     with open("claimzy-accounts_report.csv", "w") as csv_file:
          csv_writer = csv.writer(csv_file, delimiter="\t")
          csv_writer.writerow([i[0] for i in cursor.description])
          csv_writer.writerows(cursor)
          
     file_path = "claimzy-accounts_report.csv"
     print(file_path)
     if os.path.exists(file_path):
       with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response     
     return HttpResponse("Accounts Data Exported Successfully ")

 

def sendSMS(apikey, numbers,  message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,'sender' : 'CLZYIN',
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
    return render(request,'claimzy_in/admin/requests.html')

def confirm_otp(request):
     if request.session['_otp'] == int(request.GET.get('ottp')):
          return HttpResponse(request.session['_otp'])


def privacy(request):
    return render(request,'claimzy_in/client/privacy.html')

def terms(request):
    return render(request,'claimzy_in/client/terms.html')


def refunds(request):
    return render(request,'claimzy_in/client/refunds.html')

def customer_delete(request):
    id = request.GET.get('id')
    User.objects.filter(id=id).delete()
    return HttpResponse("User Deleted Successfully")

@csrf_exempt
def fetch_device(request):
     id = request.POST.get('id')
     print('Id:',id)
     dvc = Devices.objects.get(id=id)
     model = dvc.model  
     brand = dvc.brand
     #str = brand+"^"+model 
     json1={
          "brand":brand,
          "model":model
     }
     print(model,brand)
     return JsonResponse(json1)
@csrf_exempt
def send_otp(request):
     number = request.POST.get("mobile") 
     if(number == request.user.mob):
          n = random.randint(1000,9999)
          print(n)
          request.session['_otp'] = n
          message = "Verification code for Claimzy : " +str(n)
          resp =  sendSMS('9cnPqe+Y2bo-XUK0nJ6Eqv9DcYObVAe6dvr33H6fsV', number, message)
          data = json.loads(resp)
          s = json.dumps(data, indent=4, sort_keys=True)
          data = json.loads(s)
          request.session['_otp'] = n
          print(data) 
          return JsonResponse(data["status"],safe=False)
     return JsonResponse("Registered Mobile Number & Logged-In User are Different",safe=False)     

@csrf_exempt
def confirm_claim(request):
     if request.session['_otp'] == int(request.POST.get('ottp')):
          did = request.POST.get("did")
          dvc = Devices.objects.get(id=did) 
          title = request.POST.get("title")
          issue = request.POST.get("issue")
          today = datetime.now()
          d2 = today.strftime("%Y-%m-%d %H:%M:%S")
          print(did,title,issue)
          Claim.objects.create(device=dvc,mob=request.user,title=title,issue=issue,last_update=d2)
          dvc.status ="Under Claim"
          dvc.save()
          return JsonResponse("Success",safe=False)
     else:
          return JsonResponse("OTP Mismatch",safe=False)
