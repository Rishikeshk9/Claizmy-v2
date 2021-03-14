from django.db import models
from django.utils import timezone
from accounts.models import Accounts

class Claim(models.Model):
    mob = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    device = models.ForeignKey('Devices', on_delete=models.PROTECT)
    title = models.CharField(default="Other",max_length=30,choices=[('Screen Damage', 'Screen Damage'), ('Liquid Damage', 'Liquid Damage'),('Unresponsive Touchpad', 'Unresponsive Touchpad'), ('Broken Charging Port', 'Broken Charging Port'),('Faulty Earphone Jack','Faulty Earphone Jack'),('Other','Other')])
    issue = models.TextField()
    status = models.CharField(default="Under Review",max_length=30,choices=[('Under Review', 'Under Review'), ('Rejected', 'Rejected'),('Being Processed', 'Being Processed'), ('Approved', 'Approved'),('Complete', 'Complete')])
    date_posted = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(default=timezone.now)

     

class Devices(models.Model):
    mob         = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    brand       = models.CharField(max_length=100)
    model       = models.CharField(max_length=100)
    price       = models.CharField(max_length=10)
    imei        = models.CharField(max_length=100)
    plan        = models.CharField(max_length=100)
    invoice_date= models.DateField()   
    invoice     = models.FileField(upload_to='static/claimzy_in/userdata/invoice/', max_length=254,default='static/claimzy_in/img/default.jpg')
    imei_pic    = models.FileField(upload_to='static/claimzy_in/userdata/imei/', max_length=254,default='static/claimzy_in/img/default.jpg')
    front       = models.FileField(upload_to='static/claimzy_in/userdata/front/', max_length=254,default='static/claimzy_in/img/default.jpg')
    back        = models.FileField(upload_to='static/claimzy_in/userdata/back/', max_length=254,default='static/claimzy_in/img/default.jpg')
    date_posted = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(auto_now=True)
    vend        = models.CharField(max_length=10,default="",null=True,)  
    status      = models.CharField(default="Under Review",max_length=30,choices=[('Under Review', 'Under Review'),('Under Claim', 'Under Claim'), ('Rejected', 'Rejected'), ('Approved', 'Approved')])
   
     
