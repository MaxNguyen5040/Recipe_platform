def search_recipes(query, filters):
    recipes = get_all_recipes()
    if 'category' in filters:
        recipes = filter_by_category(recipes, filters['category'])
    if 'min_rating' in filters:
        recipes = filter_by_rating(recipes, filters['min_rating'])
    if 'tags' in filters:
        recipes = filter_by_tags(recipes, filters['tags'])
    return recipes

def filter_by_category(recipes, category):
    return [recipe for recipe in recipes if recipe['category'] == category]

def filter_by_rating(recipes, min_rating):
    return [recipe for recipe in recipes if recipe['rating'] >= min_rating]

def filter_by_tags(recipes, tags):
    return [recipe for recipe in recipes if set(tags).intersection(recipe['tags'])]

def get_all_recipes():
    return [
        {'title': 'Recipe 1', 'category': 'Dessert', 'rating': 4, 'tags': ['chocolate', 'easy']},
        {'title': 'Recipe 2', 'category': 'Main', 'rating': 5, 'tags': ['vegan', 'quick']}
    ]
