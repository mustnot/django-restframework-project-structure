from django.contrib.auth.hashers import check_password, is_password_usable, make_password
from django.contrib.auth.models import BaseUserManager
from django.utils.crypto import salted_hmac
from django.db import models

from common.models import TimeStampedModel


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.role = User.Role.USER
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.role = User.Role.ADMIN
        user.save(using=self._db)
        return user


class User(TimeStampedModel):
    class Status(models.IntegerChoices):
        INACTIVE = 0
        ACTIVE = 1

    class Role(models.IntegerChoices):
        ADMIN = 0, "Admin"
        USER = 1, "User"

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    role = models.PositiveIntegerField(choices=Role.choices, default=Role.USER)
    status = models.IntegerField(choices=Status.choices, default=Status.ACTIVE)

    last_login_at = models.DateTimeField(blank=True, null=True)

    _password = None

    objects = UserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.id}. {self.email}"

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """

        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)

    def set_unusable_password(self):
        # Set a value that will never be a valid hash
        self.password = make_password(None)

    def has_usable_password(self):
        """
        Return False if set_unusable_password() has been called for this user.
        """
        return is_password_usable(self.password)

    def get_session_auth_hash(self):
        """
        Return an HMAC of the password field.
        """
        key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
        return salted_hmac(
            key_salt,
            self.password,
            algorithm="sha256",
        ).hexdigest()
