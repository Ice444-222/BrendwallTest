from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, verbose_name="Название")
    description = models.TextField(max_length=256, blank=False, verbose_name="Описание")
    price = models.IntegerField(validators=[MinValueValidator(1)], blank=False, verbose_name="Цена")
