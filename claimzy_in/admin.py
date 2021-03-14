from django.contrib import admin
from .models import Claim, Devices
from accounts.models import Accounts
from django.contrib.auth.admin import UserAdmin

  
class AccountAdmin(UserAdmin):
    list_display = ('name','mob','date_joined','last_login','is_active','is_superuser','is_customer','is_vendor')
    search_fields= ('name','mob')
    readonly_fields= ('date_joined','last_updated')
    ordering = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('mob','name','address','addresstwo','city','pincode','state', 'password','date_joined','last_updated')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active','is_customer','is_vendor')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name','mob', 'password1', 'password2', 'is_staff', 'is_active','is_customer','is_vendor')}
        ),
    )
    search_fields = ('mob','name')
    ordering = ('mob',)



@admin.register(Devices)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('mob','brand','model','plan','status','date_posted')
    search_fields= ('mob','brand')
    readonly_fields= ('date_posted','last_update')
    filter_horizontal = ()
    list_filter = ()
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mob','brand','model','plan','status','date_posted','last_update')}
        ),
    )
    search_fields = ('mob','brand','model','plan','status',)
    ordering = ('date_posted',)

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('mob','device','title','issue','status','date_posted')
    search_fields= ('mob','device')
    readonly_fields= ('date_posted','last_update')
    filter_horizontal = ()
    list_filter = ()
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mob','device','title','issue','status','date_posted','last_update')}
        ),
    )
    search_fields = ('mob','device','title','issue','status')
    ordering = ('date_posted','last_update')    
admin.site.register(Accounts,AccountAdmin)
 