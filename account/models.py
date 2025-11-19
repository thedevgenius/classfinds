from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("Phone number is required")

        phone = str(phone)

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(phone, password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    phone = models.CharField(max_length=15, unique=True)
    

    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []   # phone is mandatory by default

    def __str__(self):
        return self.phone
