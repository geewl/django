from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length = 45)
    menu = models.ForeignKey('Menu', on_delete = models.CASCADE)

    class Meta:
        db_table = 'categories'

class Drink(models.Model):
    korean_name   = models.CharField(max_length = 45)
    english_name  = models.CharField(max_length = 45)
    description   = models.TextField()
    category      = models.ForeignKey('Category', on_delete = models.CASCADE)
    allergy_drink = models.ManyToManyField('Allergy')

    class Meta:
        db_table = 'drinks'

class Size(models.Model):
    name             = models.CharField(max_length = 45)
    size_ml          = models.CharField(max_length = 45)
    size_fluid_ounce = models.CharField(max_length = 45)
    drink            = models.ForeignKey('Drink', on_delete = models.CASCADE)

    class Meta:
        db_table = 'sizes'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits = 10, decimal_places = 2)
    sodium_mg        = models.DecimalField(max_digits = 10, decimal_places = 2)
    saturated_fat_g  = models.DecimalField(max_digits = 10, decimal_places = 2)
    sugars_g         = models.DecimalField(max_digits = 10, decimal_places = 2)
    protein_g        = models.DecimalField(max_digits = 10, decimal_places = 2)
    caffeine_mg      = models.DecimalField(max_digits = 10, decimal_places = 2)
    drink            = models.ForeignKey('Drink', on_delete = models.CASCADE)
    size             = models.ForeignKey('Size', on_delete = models.CASCADE)

    class Meta:
        db_table = 'nutritions'

class Image(models.Model):
    image_url = models.CharField(max_length = 2000)
    drink     = models.ForeignKey('Drink', on_delete = models.CASCADE)

    class Meta:
        db_table = 'images'

class Allergy(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'allergies'

class AllergyDrink(models.Model):
    drink   = models.ForeignKey('Drink', on_delete = models.CASCADE)
    allergy = models.ForeignKey('Allergy', on_delete = models.CASCADE)

    class Meta:
        db_table = 'allergy_drinks'
