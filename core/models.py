from django.core.validators import validate_slug
from django.db import models
from mptt import models as mptt_models


# Create your models here.
class SpecificationParameter(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


class Specification(models.Model):
    characteristic = models.ForeignKey(SpecificationParameter, on_delete=models.CASCADE)


class Category(mptt_models.MPTTModel):
    slug = models.CharField(max_length=255, help_text='This is slug', validators=[validate_slug])
    specification_id = models.ForeignKey(Specification, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, help_text='List of characteristics for products in this category')
    parent = mptt_models.TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                        related_name='children')


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, help_text='This is slug', validators=[validate_slug])
    description = models.TextField()
    price = models.DecimalField(max_digits=11, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

# TODO: Сделать модель баннеров
# TODO: Сделать модель статей
