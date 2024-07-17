class RecipeRatings:
    def __init__(self):
        self.ratings = {}

    def add_rating(self, recipe_id, rating):
        if recipe_id not in self.ratings:
            self.ratings[recipe_id] = []
        self.ratings[recipe_id].append(rating)

    def get_average_rating(self, recipe_id):
        if recipe_id in self.ratings:
            return sum(self.ratings[recipe_id]) / len(self.ratings[recipe_id])
        return None

# main.py

ratings = RecipeRatings()
ratings.add_rating(recipe_id=1, rating=5)
ratings.add_rating(recipe_id=1, rating=4)
average_rating = ratings.get_average_rating(recipe_id=1)
print(f"Average rating for recipe 1: {average_rating}")