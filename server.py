from flask import Flask, request, render_template, redirect
import os
import requests
import json

"""DEPLOYED AT http://ab-todo-app.herokuapp.com/"""

app = Flask(__name__)

TODOS = {}

@app.route('/')
def show_homepage():
    """Display homepage where user can view all of their todos."""

    # filter dictionary by completion status so user only sees incomplete todos
    incomplete_todos = {}

    for todo in TODOS:
        if TODOS[todo][0] == 'incomplete':
            incomplete_todos[todo] = ['incomplete', TODOS[todo][1]]

    return render_template('index.html', todos=incomplete_todos)


@app.route('/create-todo', methods=['POST'])
def create_todo():
    """Create new todo items with user input."""

    todo = request.form.get('todo')
    priority_level = request.form.get('priority-level')

    if todo in TODOS:
        pass
    else:
        TODOS[todo] = ['incomplete', priority_level]

    return redirect('/')


@app.route('/complete-todo', methods=['POST'])
def complete_todo():
    """Complete todo selected by user."""

    todo = request.form.get('todo')

    TODOS[todo] = 'complete'

    return redirect('/')


@app.route('/count-priorities')
def count_priorities():
    """Counts number of todos at a specific priority level."""

    priority_count = {} 

    for todo in TODOS:

        priority = TODOS[todo][1]

        if priority in priority_count:
            priority_count[priority] += 1
        else:
            priority_count[priority] = 1

    return render_template('priority_count.html', priority_count=priority_count,
                                                  missing_p_levels=missing_p_levels)


@app.route('/error')
def page_pagerduty():
    """Send JSON body to PagerDuty."""

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

    print 'ERROR MESSAGE:', r.json()

    return render_template('error.html', error_data=r.json())


if __name__ == "__main__":
    app.debug = True

    app.jinja_env.auto_reload = app.debug  

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    # Heroku provides a random port so saving in a variable
    # PORT = int(os.environ.get("PORT", 5000)) 

    app.run(host="0.0.0.0", port=3000)