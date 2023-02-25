from os import getenv
from flask import Flask
from flask import request
from flask import flash
from flask import render_template
from flask import redirect
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from sqlalchemy.exc import DatabaseError
from models import db
from werkzeug.exceptions import NotFound
from views.products import products_app
from views.users import users_app

app = Flask(
    __name__,
)
app.register_blueprint(products_app, url_prefix="/products")
app.register_blueprint(users_app, url_prefix="/users")

CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")

csft = CSRFProtect(app)

db.app = app
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)


@app.cli.command("db-create-all")
def db_create_all():
    db.create_all()


@app.get("/", endpoint="index_page")
def get_root():
    return render_template("index.html")


@app.route("/hello/")
@app.route("/hello/<name>/")
def hello_world(name: str = None):
    if name is None:
        name = request.args.get("name", "world")
    return f"<h2>Hello {name}!</h2>"


@app.errorhandler(DatabaseError)
def handle_database_error(error):
    flash("oops! no db connection!", "danger")
    return redirect("/")

@app.errorhandler(404)
def handle_404(error):
    if isinstance(error, NotFound) and error.description != NotFound.description:
        return error
    return render_template("404.html"), 404

