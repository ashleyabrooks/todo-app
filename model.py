"""Models and database functions."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///todo-app'
    db.app = app
    db.init_app(app)


class Todo(object):
    """Class for Todo item."""

    __tablename__ = 'todos'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    todo = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Convenience method to show information about todo in console."""

        return '<TODO item: %s, id=%s>' % (todo, id)


if __name__ == '__main__':
    # In case you want to run module in Python shell.

    from server import app
    connect_to_db(app)
    print "Connected to db."


