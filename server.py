from flask import Flask, request, render_template, redirect

app = Flask(__name__)

TODOS = {}

@app.route('/')
def show_homepage():
    """Display homepage where user can view all of their todos."""

    # filter dictionary by completion status so user only sees incomplete todos
    incomplete_todos = {}

    for todo in TODOS:
        if TODOS[todo] == 'incomplete':
            incomplete_todos[todo] = 'incomplete'

    return render_template('index.html', todos=incomplete_todos)


@app.route('/create-todo', methods=['POST'])
def create_todo():
    """Create new todo items with user input."""

    todo = request.form.get('todo')

    if todo in TODOS:
        pass
    else:
        TODOS[todo] = 'incomplete'

    return redirect('/')


@app.route('/complete-todo', methods=['POST'])
def complete_todo():
    """Complete todo selected by user."""

    todo = request.form.get('todo')

    TODOS[todo] = 'complete'

    return redirect('/')


if __name__ == "__main__":
    app.debug = True

    app.jinja_env.auto_reload = app.debug  

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT)