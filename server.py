from flask import Flask, request, render_template, redirect
import os

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


@app.route('/error', methods=['POST'])
def page_pagerduty():
    """Send JSON body to PagerDuty."""

    # TODO - Fix

    url = 'https://events.pagerduty.com/generic/2010-04-15/create_event.json'

    payload = {    
      "service_key": "b3afd708e7984831b9abaecff56995b6", # for learning purposes so not putting this in enviro variable
      "event_type": "trigger",
      "description": "FAILURE for production/HTTP on machine srv01.acme.com",
      "client": "Sample Monitoring Service",
      "client_url": "https://monitoring.service.com",
      "details": {
        "ping time": "1500ms",
        "load avg": 0.75
      },
      "contexts":[ 
        {
          "type": "link",
          "href": "http://acme.pagerduty.com"
        },{
          "type": "link",
          "href": "http://acme.pagerduty.com",
          "text": "View the incident on PagerDuty"
        },{
          "type": "image",
          "src": "https://chart.googleapis.com/chart?chs=600x400&chd=t:6,2,9,5,2,5,7,4,8,2,1&cht=lc&chds=a&chxt=y&chm=D,0033FF,0,0,5,1"
        }
      ]
    }

    r = requests.post(url, data=json.dumps(payload))

    print r.json()


if __name__ == "__main__":
    app.debug = True

    app.jinja_env.auto_reload = app.debug  

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT)