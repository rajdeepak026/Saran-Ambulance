from flask import Flask
from backend.database import db
app = None

def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dbname.sqlite3"
    db.init_app(app)
    app.app_context().push()
    return app

app = create_app()
from backend.controllers import *

if __name__=="__main__":
    app.run()