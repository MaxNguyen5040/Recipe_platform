def share_recipe_on_social_media(recipe_id, platform):
    recipe = get_recipe_by_id(recipe_id)
    message = f"Check out this recipe: {recipe['title']}"
    post_to_platform(platform, message)

def post_to_platform(platform, message):
    print(f"Posted to {platform}: {message}")