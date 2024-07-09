from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from app import app, db
from forms.tag_form import TagForm
from models.tag import Tag

@tag.route('/tags', methods=['GET', 'POST'])
@login_required
def manage_tags():
    form = TagForm()
    if form.validate_on_submit():
        tag = Tag(name=form.name.data)
        db.session.add(tag)
        db.session.commit()
        flash('Tag added successfully!')
        return redirect(url_for('tag.manage_tags'))
    tags = Tag.query.all()
    return render_template('manage_tags.html', form=form, tags=tags)