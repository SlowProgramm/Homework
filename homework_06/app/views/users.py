from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash,
)
from sqlalchemy.exc import IntegrityError

from werkzeug.exceptions import BadRequest
from werkzeug.exceptions import NotFound
from models import db, UserModel
from views.forms.users import CreateUserForm


users_app = Blueprint(
    "users_app",
    __name__,
)


@users_app.get("/list/", endpoint="users_list")
def users_list():
        list_of_users = UserModel.query.all()
        return render_template("user/users_list.html", list=list_of_users)


@users_app.route("/<int:product_id>", methods=["GET", "POST"], endpoint="user_details")
def user_details(product_id: int):
    user = UserModel.query.get(product_id)
    if user is None:
        raise NotFound(f"User #{product_id} not found")
    if request.method == 'GET':
        return render_template("user/user_details.html", user=user)
    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        flash(f"Deleted product {user.name}!", "warning")
        url = url_for("users_app.users_list")
        return redirect(url)


@users_app.route(
    "/add/",
    methods=["GET", "POST"],
    endpoint="add",
)
def add_product():
    form = CreateUserForm()

    if request.method == "GET":
        return render_template("user/users_add.html", form=form)

    if not form.validate_on_submit():
        return render_template("user/users_add.html"), 400

    user_name = form.name.data
    user_address = form.address.data
    user_age = form.age.data
    user = UserModel(name=user_name, age=user_age, address=user_address)
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest(f"Could not create product {user_name!r},"
                         f" probably such product already exists.")
    flash(f"Successfully added product {user_name}!")
    url = url_for("users_app.user_details", product_id=user.id)
    return redirect(url)
