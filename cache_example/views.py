# Create your views here.
from django.views.generic import ListView

from cache_example.models import Recipe, Ingredient


class RecipeView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipes_list.html'

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(RecipeView, self).get_context_data(**kwargs)
    #
    #     # Create any data and add it to the context
    #     context['ingredients'] = context['recipes'].ingredients
    #     return context

class IngredientView(ListView):
    model = Ingredient
    context_object_name = 'ingredients'
    template_name = 'ingredients_list.html'


