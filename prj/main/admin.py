from django.contrib import admin
from .models import Cuisine, Recipe, Category

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty_stars', 'calories', 'cuisine')
    readonly_fields = ('difficulty_stars',)
    
admin.site.register(Cuisine)
admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)