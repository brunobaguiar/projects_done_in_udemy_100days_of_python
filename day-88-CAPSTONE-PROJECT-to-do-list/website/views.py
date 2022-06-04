from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Task
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        task = request.form.get('task')

        if len(task) < 1:
            flash('task is too short!', category='error')
        else:
            new_task = Task(data=task, user_id=current_user.id)
            db.session.add(new_task)
            db.session.commit()
            flash('task added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/update-task/<int:task_id>')
def update_task(task_id):
    task = Task.query.get(task_id)
    task.status = not task.status
    db.session.commit()
    return redirect(url_for("views.home"))


@views.route('/delete-task/<int:task_id>')
def delete_task(task_id):
    task_to_delete = Task.query.get(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for("views.home"))

