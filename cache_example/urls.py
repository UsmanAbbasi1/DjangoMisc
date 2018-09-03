from django.urls import path

from cache_example import views

urlpatterns = [
    path('recipes', views.RecipeView.as_view(), name='recipes'),
    path('ingredients',views.IngredientView.as_view(), name = 'ingredients')

]
