from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length


class CreateUserForm(FlaskForm):
    name = StringField(
        label="User name",
        name="user-name",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
    age = IntegerField(
        label="User age",
        name="user-age",
        validators=[
            DataRequired(),
        ],
    )
    address = StringField(
        label="User address",
        name="user-address",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )

    # description = TextAreaField(validators=[DataRequired()])