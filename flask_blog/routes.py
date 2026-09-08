from flask import render_template, url_for,flash,redirect
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog import app
from flask_blog.models import User, Post



posts = [
    {
        'author':'Nathaniel Agbodzi',
        'title' : 'The Winner',
        'content': 'First post content',
        'date_posted' : 'April 20, 2026'
    },

    {
        'author':'Emmanuel Asare',
        'title' : 'The Histle',
        'content': 'Second post content',
        'date_posted' : 'April 20, 2023'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm() 
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))


    return render_template('register.html', form=form ,title="Register")



@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "nathaniel@gmail.com" and form.password.data == "password":
            flash(f'Logged in as {form.email.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('login.html', title ='Login', form=form)