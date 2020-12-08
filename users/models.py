from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(validators=[MinLengthValidator(5)], max_length=250)
    gender = models.CharField(max_length=1)  # 'F' -> female, 'M' -> male
    birth_date = models.DateField(default=timezone.now())
    monthly_limit = models.FloatField(null=True, blank=True, default=None)
    income_range = models.ForeignKey(
        'commons.IncomeRange',
        on_delete=models.SET_NULL,
        null=True
    )
