class BookmarkingSystem:
    def __init__(self):
        self.bookmarks = {}

    def bookmark_recipe(self, user, recipe):
        if user not in self.bookmarks:
            self.bookmarks[user] = []
        if recipe not in self.bookmarks[user]:
            self.bookmarks[user].append(recipe)

    def get_bookmarked_recipes(self, user):
        return self.bookmarks.get(user, [])

bookmarks = BookmarkingSystem()
bookmarks.bookmark_recipe(user1, recipe)
user_bookmarks = bookmarks.get_bookmarked_recipes(user1)
for bookmarked_recipe in user_bookmarks:
    print(f"Bookmarked Recipe: {bookmarked_recipe.name}")
