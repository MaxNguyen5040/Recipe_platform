from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from app import app, db
from models.recipe import Recipe
from forms.recipe_form import RecipeForm

@recipe.route('/recipe/new', methods=['GET', 'POST'])
@login_required
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(title=form.title.data, ingredients=form.ingredients.data, instructions=form.instructions.data, author_id=current_user.id)
        db.session.add(recipe)
        db.session.commit()
        flash('Your recipe has been created!')
        return redirect(url_for('index'))
    return render_template('create_recipe.html', form=form)

@recipe.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template('recipe_detail.html', recipe=recipe)

@recipe.route('/recipe/<int:recipe_id>/update', methods=['GET', 'POST'])
@login_required
def update_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.author_id != current_user.id:
        abort(403)
    form = RecipeForm()
    if form.validate_on_submit():
        recipe.title = form.title.data
        recipe.ingredients = form.ingredients.data
        recipe.instructions = form.instructions.data
        db.session.commit()
        flash('Your recipe has been updated!')
        return redirect(url_for('recipe.recipe_detail', recipe_id=recipe.id))
    elif request.method == 'GET':
        form.title.data = recipe.title
        form.ingredients.data = recipe.ingredients
        form.instructions.data = recipe.instructions
    return render_template('create_recipe.html', form=form, legend='Update Recipe')

@recipe.route('/recipe/<int:recipe_id>/delete', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.author_id != current_user.id:
        abort(403)
    db.session.delete(recipe)
    db.session.commit()
    flash('Your recipe has been deleted!')
    return redirect(url_for('index'))
