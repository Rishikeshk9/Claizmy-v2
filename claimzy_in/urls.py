
from django.urls import path
from claimzy_in import views
from accounts import views as user_views
from django.contrib.auth.models import User

urlpatterns = [
    path('', views.claimzy, name='claimzy'),
    path('test/', views.test, name='claimzy-test'),
    path('admin-user/', views.home, name='claimzy-home'),
    path('about/', views.about, name='claimzy-about'),
    path('users/', views.users, name='claimzy-users'),
    path('vendors/', views.vendors, name='claimzy-vendors'),
    path('devices/', views.devices, name='claimzy-devices'),
    path('reports/', views.download_report, name='download-reports'),
    path('users/profile', views.usersdetails, name='claimzy-usersdetails'),
    path('profile-customer', views.custdetails, name='claimzy-profilecust'),
    path('update-profile', views.updateprofile, name='claimzy-profileupdate'),
    path('users/myprofile', views.mydetails, name='claimzy-mydetails'),
    path('map/', views.map, name='claimzy-map'),
    path('logout/', user_views.logout_view, name='claimzy-logout'),
    path('claim/', views.user_claims, name='claim'),
    path('manage/',views.claim_status,name='manage'),
    path('request-manage/',views.request_status,name='manage-request'),
    path('register-device/',views.device_register,name='device-register'),
    path('image/',views.image_register,name='image-register'),
    path('request/',views.requests,name='requests'),
    path('request-otp/',views.otp,name='requests-otp'),
    path('confirm-otp/',views.confirm_otp,name='confirm-image-otp'),
    path('user-register/',views.user_register,name='user-register'),
    path('upload-files/',views.upload_file,name='upload-data'),
    path('privacy/',views.privacy,name='privacy'),
    path('terms/',views.terms,name='terms'),
    path('refunds/',views.refunds,name='refunds'),
    path('delete/',views.customer_delete,name='customer-delete'),
    path('capture/',views.capture,name='capture-payment'),
    path('verify/',views.verify,name='verify-payment'),
    path('status/',views.status,name='status-payment'),
    path('fetch/',views.fetch_device,name='fetch-device'),
    path('sendotp/',views.send_otp,name='send-otp'),
    path('confclaim/',views.confirm_claim,name='confirm-claim'),
 
 ]
