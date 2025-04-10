from flask import render_template, redirect, url_for, request, flash
from app import db
from app.models import Task
from app.forms import TaskForm
from flask import Blueprint
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)

@bp.route('/add_task', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data
        )
        db.session.add(task)
        db.session.commit()
        flash('Task added successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('add_task.html', form=form)

@bp.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.due_date = form.due_date.data
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('add_task.html', form=form, task=task)

@bp.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('main.index'))

@bp.route('/toggle_task/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('main.index'))