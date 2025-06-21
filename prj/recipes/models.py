from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    CUISINE_CHOICES = [
        ('czech', 'Czech'),
        ('italian', 'Italian'),
        ('french', 'French'),
        ('indian', 'Indian'),
        ('chinese', 'Chinese'),
        ('japanese', 'Japanese'),
    ]

    name = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=20, choices=CUISINE_CHOICES)
    categories = models.ManyToManyField(Category, blank=True)
    calories = models.PositiveIntegerField()
    proteins = models.FloatField(null=True, blank=True)  # bílkoviny (g)
    fats = models.FloatField(null=True, blank=True)     # tuky (g)
    carbs = models.FloatField(null=True, blank=True)    # sacharidy (g)
    difficulty = models.PositiveSmallIntegerField()  # 1–5
    description = models.TextField()
    instructions = models.TextField(help_text="Postup vaření")
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    amount = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.amount} {self.name}"
