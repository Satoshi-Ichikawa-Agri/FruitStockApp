import uuid
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

from apps.models.mixin import BaseMixin


class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, user_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth, user_name, and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        if not user_name:
            raise ValueError("Users must have a user name")

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            user_name=user_name,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, date_of_birth, user_name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth, user_name, and password.
        """
        user = self.create_user(
            email,
            date_of_birth=date_of_birth,
            user_name=user_name,
            password=password,
        )
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin, BaseMixin):
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    user_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name", "date_of_birth"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
