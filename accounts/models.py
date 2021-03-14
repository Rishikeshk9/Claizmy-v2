from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self,mob,name,address,addresstwo,city,pincode,state,password=None):
        if not mob:
            raise ValueError("User must have a mobile Number")
        if not name:
            raise ValueError("User must have Name")
        if not address:
            raise ValueError("User must have Address")
         

        user =  self.model(
                name    = name,
                address = address,
                addresstwo = addresstwo,
                city = city,
                pincode = pincode,
                state = state,
                mob     = mob,
                 
            )
        user.set_password(password)     
        user.is_active       = True
        user.save(using=self._db)
        return user 

    def create_customer(self,mob,name,address,addresstwo,city,pincode,state,password=None):
        if not mob:
            raise ValueError("User must have a mobile Number")
        if not name:
            raise ValueError("User must have Name")
        if not address:
            raise ValueError("User must have Address")
         

        user =  self.model(
                name    = name,
                address = address,
                addresstwo = addresstwo,
                city = city,
                pincode = pincode,
                state = state,
                mob     = mob,
            )
        user.set_password(password)     
        user.is_active  = True
        user.save(using=self._db)
        return user      

    def create_superuser(self,  mob, name, address,password):
        user =  self.create_user(
                
                name = name,
                address = address,
                mob = mob,
                password = password
            )
        user.is_superuser    = True
        user.is_active       = True
        user.is_staff        = True
        user.is_customer     = False   
        user.save(using=self._db)
        return user  


# Create your models here.
class Accounts(AbstractBaseUser):
    mob             = models.CharField(max_length=10, unique=True)
    name            = models.CharField(max_length=30, editable=True)
    address         = models.CharField(max_length=100)
    addresstwo       = models.CharField(max_length=50,default="address")
    city            = models.CharField(max_length=20,default="Pune")
    pincode         = models.CharField(max_length=6,default="000000")
    state           = models.CharField(max_length=30,default="Maharashtra",choices=[('Andhra Pradesh','Andhra Pradesh'),('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),('Arunachal Pradesh','Arunachal Pradesh'),('Assam','Assam'),('Bihar','Bihar'),('Chandigarh','Chandigarh'),('Chhattisgarh','Chhattisgarh'),('Dadar and Nagar Haveli','Dadar and Nagar Haveli'),('Daman and Diu','Daman and Diu'),('Delhi','Delhi'),('Lakshadweep','Lakshadweep'),('Puducherry','Puducherry'),('Goa','Goa'),('Gujarat','Gujarat'),('Haryana','Haryana'),('Himachal Pradesh','Himachal Pradesh'),('Jammu and Kashmir','Jammu and Kashmir'),('Jharkhand','Jharkhand'),('Karnataka','Karnataka'),('Kerala','Kerala'),('Madhya Pradesh','Madhya Pradesh'),('Maharashtra','Maharashtra'),('Manipur','Manipur'),('Meghalaya','Meghalaya'),('Mizoram','Mizoram'),('Nagaland','Nagaland'),('Odisha','Odisha'),('Punjab','Punjab'),('Rajasthan','Rajasthan'),('Sikkim','Sikkim'),('Tamil Nadu','Tamil Nadu'),('Telangana','Telangana'),('Tripura','Tripura'),('Uttar Pradesh','Uttar Pradesh'),('Uttarakhand','Uttarakhand'),('West Bengal','West Bengal')])

    date_joined     = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_updated      = models.DateTimeField(verbose_name="last updated",auto_now=True)
    is_superuser    = models.BooleanField(default=False)
    is_vendor       = models.BooleanField(default=False)
    is_customer     = models.BooleanField(default=True)
    is_active       = models.BooleanField(default=True)
    is_staff       = models.BooleanField(default=False)

    USERNAME_FIELD  = 'mob'
    
    REQUIRED_FIELDS = ['name','address']

    objects = MyAccountManager()

    def __str__(self):
        return self.mob

    def has_perm(self,perm,obj=None):
        return self.is_superuser

    def has_module_perms(self,app_label):
        return True
 

        