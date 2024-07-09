from app import db
from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from app import app, db
from forms.category_form import CategoryForm
from models.category import Category

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    def __repr__(self):
        return f'<Category {self.name}>'

from app import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    def __repr__(self):
        return f'<Tag {self.name}>'
    
@category.route('/categories', methods=['GET', 'POST'])
@login_required
def manage_categories():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data)
        db.session.add(category)
        db.session.commit()
        flash('Category added successfully!')
        return redirect(url_for('category.manage_categories'))
    categories = Category.query.all()
    return render_template('manage_categories.html', form=form, categories=categories)