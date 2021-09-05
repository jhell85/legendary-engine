from django.contrib import admin
from .models import User as MyUser
from django.contrib.auth.admin import UserAdmin

ADDITIONAL_USER_FIELDS = (
    (None, {'fields': ('profile_pic',)}),
)

class MyUserAdmin(UserAdmin):
    model = MyUser

    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS

admin.site.register(MyUser, MyUserAdmin)