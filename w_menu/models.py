from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Product(models.Model):
    
    class Meta(object):

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    title = models.CharField(
        max_length=256,
        blank=True,
        unique=True,
        verbose_name='title'
    )

    available = models.BooleanField(
        verbose_name='available'
    )

    notes = models.TextField(
        blank=True,
        null=True,
        verbose_name='notes'
    )

    def __str__(self):
        return f'{self.title}'


class Dish(models.Model):
    
    class Meta(object):

        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'

    title = models.CharField(
        max_length=256,
        blank=False,
        unique=True,
        verbose_name='titile'
    )

    product = models.ManyToManyField(Product,
        max_length=256,
        blank=True,
        verbose_name='title'
    )
    
    def __str__(self):
        return f'{self.title}'


# don't migrated Menu
class Menu(models.Model):

    class Meta(object):

        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='title'
    )

    dish = models.ManyToManyField(Dish,
        max_length=256,
        blank=True,
        verbose_name='dish'
    )


class DishComposition(models.Model):

    class Meta(object):

        verbose_name = 'DishComposition'
        verbose_name_plural = 'DishCompositions'

    dish = models.ForeignKey(Dish,
        verbose_name='Dish',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    product = models.ForeignKey(Product,
        verbose_name='Product',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

