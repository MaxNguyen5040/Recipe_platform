from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SECRET_KEY'] = 'mysecret'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route('/edit_recipe/<int:recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if request.method == 'POST':
        recipe.title = request.form['title']
        recipe.ingredients = request.form['ingredients']
        recipe.instructions = request.form['instructions']
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('edit_recipe.html', recipe=recipe)

@app.route('/delete_recipe/<int:recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for('dashboard'))

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get_or_404(session['user_id'])
    recipes = Recipe.query.filter_by(user_id=user.id).all()
    return render_template('profile.html', user=user, recipes=recipes)

@app.route('/rate_recipe/<int:recipe_id>', methods=['POST'])
def rate_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    rating = request.form['rating']
    user_id = session['user_id']
    new_rating = Rating(rating=rating, user_id=user_id, recipe_id=recipe_id)
    db.session.add(new_rating)
    db.session.commit()
    return redirect(url_for('recipe', recipe_id=recipe_id))

@app.route('/submit_recipe', methods=['GET', 'POST'])
def submit_recipe():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        user_id = session['user_id']
        new_recipe = Recipe(title=title, ingredients=ingredients, instructions=instructions, user_id=user_id)
        db.session.add(new_recipe)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('submit_recipe.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = Recipe.query.filter(Recipe.title.contains(query) | Recipe.ingredients.contains(query)).all()
    return render_template('search_results.html', results=results, query=query)

@app.route('/add_comment/<int:recipe_id>', methods=['POST'])
def add_comment(recipe_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    content = request.form['content']
    user_id = session['user_id']
    new_comment = Comment(content=content, user_id=user_id, recipe_id=recipe_id)
    db.session.add(new_comment)
    db.session.commit()
    return redirect(url_for('recipe', recipe_id=recipe_id))

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        user = User.query.get(session['user_id'])
        if user.check_password(old_password):
            user.set_password(new_password)
            db.session.commit()
            return redirect(url_for('profile'))
        else:
            return "Incorrect old password."
    return render_template('change_password.html')

@app.route('/add_favorite/<int:recipe_id>', methods=['POST'])
def add_favorite(recipe_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    favorite = Favorite(user_id=user_id, recipe_id=recipe_id)
    db.session.add(favorite)
    db.session.commit()
    return redirect(url_for('recipe', recipe_id=recipe_id))

@app.route('/favorites')
def favorites():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    favorites = Favorite.query.filter_by(user_id=user_id).all()
    favorite_recipes = [f.recipe for f in favorites]
    return render_template('favorites.html', recipes=favorite_recipes)

@app.route('/share_recipe/<int:recipe_id>', methods=['POST'])
def share_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    email = request.form['email']
    recipe = Recipe.query.get_or_404(recipe_id)
    # Implement email sending logic here
    send_email(email, f"Check out this recipe: {recipe.title}", f"Ingredients: {recipe.ingredients}\nInstructions: {recipe.instructions}")
    return redirect(url_for('recipe', recipe_id=recipe_id))

@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('add_category.html')

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    categories = Category.query.all()
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        category_id = request.form['category_id']
        user_id = session['user_id']
        new_recipe = Recipe(title=title, ingredients=ingredients, instructions=instructions, user_id=user_id, category_id=category_id)
        db.session.add(new_recipe)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('add_recipe.html', categories=categories)
 
@app.route('/top_rated')
def top_rated():
    recipes = Recipe.query.all()
    recipes = sorted(recipes, key=lambda r: sum(rt.rating for rt in r.ratings) / len(r.ratings) if r.ratings else 0, reverse=True)
    return render_template('top_rated.html', recipes=recipes)

@app.route('/add_tag', methods=['GET', 'POST'])
def add_tag():
    if request.method == 'POST':
        name = request.form['name']
        new_tag = Tag(name=name)
        db.session.add(new_tag)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('add_tag.html')

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    categories = Category.query.all()
    tags = Tag.query.all()
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        category_id = request.form['category_id']
        tag_ids = request.form.getlist('tag_ids')
        image_file = save_picture(request.files['image_file'])
        user_id = session['user_id']
        new_recipe = Recipe(
            title=title,
            ingredients=ingredients,
            instructions=instructions,
            user_id=user_id,
            category_id=category_id,
            image_file=image_file
        )
        new_recipe.tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
        db.session.add(new_recipe)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('add_recipe.html', categories=categories, tags=tags)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/recipe_pics', picture_fn)
    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn
