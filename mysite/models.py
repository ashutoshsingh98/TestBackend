from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class M_userManager(BaseUserManager):
    def create_user(self, real_name, eid, tz, password=None):
        if not real_name:
            raise ValueError("Users must have Unique Usernames")
        if not id:
            raise ValueError("Users must have valid Contacts")
        if not tz:
            raise ValueError("Users must have their First Name")
        user = self.model(eid=eid, real_name=real_name, tz=tz)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, eid, real_name, tz, password):
        user = self.create_user(eid=eid, real_name=real_name, tz=tz, password=password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class M_user(AbstractBaseUser):
    real_name = models.CharField(max_length=100, unique=True)
    eid = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)
    REQUIRED_FIELDS = ['eid', 'tz']
    USERNAME_FIELD = 'real_name'
    objects = M_userManager()
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    def __str__(self):
        return self.eid + ", " + self.real_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Activity(models.Model):
    member_id = models.ForeignKey(M_user, related_name='activities', on_delete=models.CASCADE)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)


    def __str__(self):
        return self.member_id.real_name
