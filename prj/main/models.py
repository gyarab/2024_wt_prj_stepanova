from django.db import models
from django.utils.html import mark_safe
    
class Cuisine(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        (1, '★☆☆'),
        (2, '★★☆'),
        (3, '★★★')
    ]
    name = models.CharField(max_length=300)
    difficulty = models.SmallIntegerField(choices=DIFFICULTY_CHOICES)
    calories = models.IntegerField()
    nutrition_table = models.JSONField()
    ingredients = models.JSONField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)

    cuisine = models.ForeignKey("Cuisine", on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(Category)

    def difficulty_stars(self):
        return mark_safe("★" * self.difficulty + "☆" * (3 - self.difficulty))

    def __str__(self):
        return f"{self.name} ({'★' * self.difficulty + '☆' * (3 - self.difficulty)})"