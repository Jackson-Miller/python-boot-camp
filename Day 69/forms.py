from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length, URL
from flask_ckeditor import CKEditorField


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=10, max=150), EqualTo("password_confirm", message="Passwords must match.")])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=10, max=150)])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = EmailField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit")
