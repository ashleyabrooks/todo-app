from flask import Flask, request, render_template
from model import Todo, connect_to_db, db

app = Flask(__name__)

@app.route('/')
def show_homepage():
    """Display homepage where user can view all of their todos."""

    return render_template('index.html')


@app.route('/create-todo', methods=['POST'])
def create_todo():
    """Create new todo items with user input."""

    todo = request.form.get('todo')

    new_todo = Todo(todo=todo)

    # Need to add new Todo object to session before committing to database
    db.session.add(new_todo)
    db.session.commit()

    return redirect('/')

@app.route('/delete-todo', methods=['DELETE'])
def delete_todo():
    """Delete todo selected by user."""

    todo = Todo.query.get(id)
    
    db.session.delete(todo)
    db.session.commit()


if __name__ == "__main__":
    app.debug = True

    app.jinja_env.auto_reload = app.debug  

    connect_to_db(app)

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.run(port=3000, host='0.0.0.0')