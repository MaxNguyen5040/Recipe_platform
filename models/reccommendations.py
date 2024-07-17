class RecipeRecommendations:
    def __init__(self, user, recipes):
        self.user = user
        self.recipes = recipes

    def recommend_by_past_interactions(self):
        liked_cuisines = set()
        for recipe in self.user.liked_recipes:
            liked_cuisines.add(recipe.cuisine)
        
        recommendations = []
        for recipe in self.recipes:
            if recipe.cuisine in liked_cuisines and recipe not in self.user.liked_recipes:
                recommendations.append(recipe)
        return recommendations

recommendations = RecipeRecommendations(current_user, recipe_manager.get_all_recipes())
recommended_recipes = recommendations.recommend_by_past_interactions()
for recipe in recommended_recipes:
    print(f"Recommended Recipe: {recipe.name}, Cuisine: {recipe.cuisine}")