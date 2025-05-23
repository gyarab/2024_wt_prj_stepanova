from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Recipe, Cuisine, Category

def homepage(request):
    """Homepage with featured recipes"""
    recipes = Recipe.objects.all()[:6]  # Get first 6 recipes
    return render(request, 'main/homepage.html', {'recipes': recipes})

def search_recipes(request):
    """Search functionality"""
    query = request.GET.get('q', '')
    recipes = Recipe.objects.all()
    
    if query:
        recipes = recipes.filter(
            Q(name__icontains=query) |
            Q(ingredients__icontains=query) |
            Q(instructions__icontains=query)
        )
    
    context = {
        'recipes': recipes,
        'query': query,
        'search_performed': bool(query)
    }
    return render(request, 'main/search_results.html', context)

def cuisine_recipes(request, cuisine_name):
    """Show recipes by cuisine"""
    cuisine = get_object_or_404(Cuisine, name__iexact=cuisine_name)
    recipes = Recipe.objects.filter(cuisine=cuisine)
    
    # Get filter parameters
    category_filter = request.GET.get('category')
    difficulty_filter = request.GET.get('difficulty')
    
    if category_filter:
        recipes = recipes.filter(categories__id=category_filter)
    if difficulty_filter:
        recipes = recipes.filter(difficulty=difficulty_filter)
    
    categories = Category.objects.all()
    
    context = {
        'cuisine': cuisine,
        'recipes': recipes,
        'categories': categories,
        'selected_category': category_filter,
        'selected_difficulty': difficulty_filter,
        'difficulty_choices': Recipe.DIFFICULTY_CHOICES
    }
    
    template_name = f'main/{cuisine_name.lower()}.html'
    return render(request, template_name, context)

def recipe_detail(request, recipe_id):
    """Show recipe details"""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    context = {
        'recipe': recipe
    }
    return render(request, 'main/details.html', context)