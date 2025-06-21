from django.contrib import admin
from .models import Recipe, Ingredient, Category

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine', 'calories', 'difficulty')
    list_filter = ('cuisine', 'categories')
    search_fields = ('name', 'description')
    inlines = [IngredientInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
