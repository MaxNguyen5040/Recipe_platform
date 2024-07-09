import pytest
from app import app, db
from models.user import User
from models.recipe import Recipe

def test_user_model():
    user = User(username='testuser', email='test@example.com', password_hash='hashed_password')
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'

def test_recipe_model():
    recipe = Recipe(title='Test Recipe', ingredients='Test Ingredients', instructions='Test Instructions', author_id=1)
    assert recipe.title == 'Test Recipe'
    assert recipe.ingredients == 'Test Ingredients'
    assert recipe.instructions == 'Test Instructions'