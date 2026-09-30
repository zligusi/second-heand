from django.db import models
from django.contrib.auth.models import AbstractBaseUser, \
BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, **extra_fields):
        if not email :
            raise ValueError('The email field must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, 
                          last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(useing=self._db)


    def create_superuser(self,email, first_name, last_name, password, **extra_fields ):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
                    raise ValueError('Superuser must have is_superuser=True.')


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=150)
    phone = models.CharField(max_length=13, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=50, db_index=True)
    last_name = models.CharField(max_length=50, db_index=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    nova_post = models.CharField(max_length=250, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['first_name', 'last_name']

    def __str__(self):
        return self.email
