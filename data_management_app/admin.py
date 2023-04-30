from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import ValveDetails, ValveInspection, myjoinedtable, ValvePreservation
 
# Register your models here.
class UserModel(UserAdmin):
    pass
 
 
admin.site.register(ValveDetails)
admin.site.register(ValveInspection)
admin.site.register(myjoinedtable)
admin.site.register(ValvePreservation)