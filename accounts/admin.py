from django.contrib import admin
from accounts.models import UserAccount, UserAccountManager, AbstractBaseUser
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'phonenumber', 'password']

admin.site.register(UserAccount, UserAdmin)