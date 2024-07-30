from django.contrib import admin
from formlogin.models import patient
from formlogin.models import doctor
# Register your models here.

class pateintAdmin(admin.ModelAdmin):
    list_display=('p_Firstname','p_Lastname','p_Picture','p_Username','p_EmailId','p_Password','p_AddressLi','p_City','p_State','p_Pincode')

class doctorAdmin(admin.ModelAdmin):
    list_display=('d_Firstname','d_Lastname','d_Picture','d_Username','d_EmailId','d_Password','d_AddressLi','d_City','d_State','d_Pincode')

admin.site.register(patient,pateintAdmin)
admin.site.register(doctor,doctorAdmin)