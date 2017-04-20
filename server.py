from flask import Flask, request, render_template, redirect

app = Flask(__name__)

todos = []

@app.route('/')
def show_homepage():
    """Display homepage where user can view all of their todos."""

    return render_template('index.html', todos=todos)


@app.route('/create-todo', methods=['POST'])
def create_todo():
    """Create new todo items with user input."""

    todo = request.form.get('todo')

    # if todos == {}:
    #     todo_index = 0
    # else:
    #     todo_index = 1 + max(todos.keys())

    # todos[todo_index] = todo

    todos.append(todo)

    return redirect('/')

@app.route('/update-todo', methods=['PATCH'])
def update_todo():
    """Update todo."""

    pass

@app.route('/delete-todo', methods=['DELETE'])
def delete_todo():
    """Delete todo selected by user."""

    todo = Todo.query.get(id)



if __name__ == "__main__":
    app.debug = True

    app.jinja_env.auto_reload = app.debug  

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.run(port=4000, host='0.0.0.0')