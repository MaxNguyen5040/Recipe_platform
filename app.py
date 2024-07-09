from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from views import auth, recipe, category, profile

app.register_blueprint(auth.bp)
app.register_blueprint(recipe.bp)
app.register_blueprint(category.bp)
app.register_blueprint(profile.bp)

if __name__ == '__main__':
    app.run(debug=True)
