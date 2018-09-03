# Create your views here.
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView

from cache_example.models import Recipe, Ingredient


@method_decorator(cache_page(settings.CACHE_TTL), name='dispatch')
class RecipeView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipes_list.html'

    def get_queryset(self):
        # Use prefetch_related to save queries when template access ingredients for every recipe
        return Recipe.objects.all().prefetch_related('ingredients')


@method_decorator(cache_page(settings.CACHE_TTL), name='dispatch')
class IngredientView(ListView):
    model = Ingredient
    context_object_name = 'ingredients'
    template_name = 'ingredients_list.html'
