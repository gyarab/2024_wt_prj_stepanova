from django.contrib import admin
from .models import Recipe
from .models import Cuisine

class RecipeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "difficulty", "calories"]

class CuisineAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

# Register your models here.
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Cuisine, CuisineAdmin)