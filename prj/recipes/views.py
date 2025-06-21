from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category

def home(request):
    categories = Category.objects.all()  # Všechny kategorie z DB
    recipes = Recipe.objects.all()

    # Volitelné filtrování podle kategorie a řazení i na homepage
    category_name = request.GET.get('category', 'all').lower()
    if category_name != 'all':
        recipes = recipes.filter(categories__name__iexact=category_name)
    
    sort = request.GET.get('sort', 'default')
    if sort == 'difficulty':
        recipes = recipes.order_by('difficulty')
    elif sort == 'calories':
        recipes = recipes.order_by('calories')

    return render(request, 'home.html', {
        'recipes': recipes,
        'categories': categories,
        'selected_cuisine': '',   # Žádná konkrétní kuchyně na homepage
        'selected_category': category_name,
        'selected_sort': sort,
    })

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def cuisine_view(request, cuisine_name):
    categories = Category.objects.all()
    recipes = Recipe.objects.filter(cuisine__iexact=cuisine_name)

    category_name = request.GET.get('category', 'all').lower()
    if category_name != 'all':
        recipes = recipes.filter(categories__name__iexact=category_name)
    
    sort = request.GET.get('sort', 'default')
    if sort == 'difficulty':
        recipes = recipes.order_by('difficulty')
    elif sort == 'calories':
        recipes = recipes.order_by('calories')

    return render(request, 'cuisine.html', {
        'recipes': recipes,
        'selected_cuisine': cuisine_name,
        'categories': categories,
        'selected_category': category_name,
        'selected_sort': sort,
        'cuisine_name': cuisine_name,
    })
