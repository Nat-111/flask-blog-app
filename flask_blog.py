from flask import Flask,render_template, url_for,flash,redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = '68458e7333a24309f489ddf6c224cc13'
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

if __name__ == ("__main__"):
    app.run(debug=True)