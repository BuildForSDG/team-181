from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, phonenumber, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, phonenumber=phonenumber)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, phonenumber, password=None):
        user = self.create_user(email, username, phonenumber, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff   = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phonenumber']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
    
    def __str__(self):
        return self.email
      
