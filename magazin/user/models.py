from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise TypeError('Users must have a username.')

        if not email:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Модель пользователя
    """
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=120,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='Почта',
        max_length=150,
        unique=True,
    )
    city = models.CharField(
        verbose_name='Город',
        max_length=120,
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Является активным'
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='Является админом'
    )
    is_moderator = models.BooleanField(
        default=False,
        verbose_name='Является модератором'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата регистрации'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    ip_address = models.CharField(
        verbose_name='Internet-Protocol пользователя',
        max_length=120,
        blank=True,
        null=True,
    )
    сoupons_user = models.ManyToManyField(
        'Coupon',
        verbose_name='Купоны',
        related_name='сoupons_user',
        blank=True,
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_absolute_url(self):
        return reverse('view_user', kwargs={'pk': self.pk})

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Coupon(models.Model):
    """
    Модель купона
    """
    code_сoupon = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    valid_to = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления купона'
    )
    discount_сoupon = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(25000)]
    )
    active = models.BooleanField()

    def __str__(self):
        return str(self.code_сoupon)

    class Meta:
        verbose_name = 'Coupon'
        verbose_name_plural = 'Coupons'
