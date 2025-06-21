from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Recipe, Category

def home(request):
    categories = Category.objects.all()
    recipes = Recipe.objects.all()

    search_query = request.GET.get('q', '').strip()
    if search_query:
        recipes = recipes.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(ingredients__name__icontains=search_query)
        ).distinct()

    category_name = request.GET.get('category', '').strip()
    if category_name:
        recipes = recipes.filter(categories__name__iexact=category_name)
    
    sort = request.GET.get('sort', '').strip()
    if sort == 'difficulty_asc':
        recipes = recipes.order_by('difficulty')
    elif sort == 'difficulty_desc':
        recipes = recipes.order_by('-difficulty')
    elif sort == 'calories_asc':
        recipes = recipes.order_by('calories')
    elif sort == 'calories_desc':
        recipes = recipes.order_by('-calories')
    else:
        recipes = recipes.order_by('name') 

    return render(request, 'home.html', {
        'recipes': recipes,
        'categories': categories,
        'selected_category': category_name,
        'selected_sort': sort,
        'search_query': search_query,
    })

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def cuisine_view(request, cuisine_name):
    categories = Category.objects.all()
    recipes = Recipe.objects.filter(cuisine__iexact=cuisine_name)

    category_name = request.GET.get('category', '').strip()
    if category_name:
        recipes = recipes.filter(categories__name__iexact=category_name)
    
    sort = request.GET.get('sort', '').strip()
    if sort == 'difficulty_asc':
        recipes = recipes.order_by('difficulty')
    elif sort == 'difficulty_desc':
        recipes = recipes.order_by('-difficulty')
    elif sort == 'calories_asc':
        recipes = recipes.order_by('calories')
    elif sort == 'calories_desc':
        recipes = recipes.order_by('-calories')
    else:
        recipes = recipes.order_by('name')  

    return render(request, 'cuisine.html', {
        'recipes': recipes,
        'selected_cuisine': cuisine_name,
        'categories': categories,
        'selected_category': category_name,
        'selected_sort': sort,
        'cuisine_name': cuisine_name,
    })