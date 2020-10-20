from flask import render_template, url_for, flash, redirect
from head import app,db,bcrypt
from head.forms import RegistrationForm, LoginForm, skills, details, workhistory, education
from head.models import User

@app.route("/")
@app.route("/home", methods=['get', 'post'])
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/SignUp", methods=['GET', 'POST'])
def SignUp():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!You are now able to log in', 'success')
        return redirect(url_for('SignIn'))
    return render_template('SignUp.html', title='Register', form=form)


@app.route("/SignIn", methods=['GET', 'POST'])
def SignIn():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('SignIn.html', form=form)

@app.route("/details", methods=['GET', 'POST'])
def details1():
    form = details()
    if form.validate_on_submit():
        flash(f'Step-1 Completed', 'success')
        return redirect(url_for('education1'))
    return render_template('details.html', form=form, x='details')

@app.route("/education", methods=['GET', 'POST'])
def education1():
    form = education()
    if form.validate_on_submit():
        flash(f'Step-2 Completed!', 'success')
        return redirect(url_for('skills1'))
    return render_template('education.html', form=form, x='education')

@app.route("/skills", methods=['GET', 'POST'])
def skills1():
    form = skills()
    if form.validate_on_submit():
        flash(f'Step-3 Completed', 'success')
        return redirect(url_for('workexp1'))
    return render_template('skills.html', form=form, x='skills')

@app.route("/workexp", methods=['GET', 'POST'])
def workexp1():
    form = workhistory()
    if form.validate_on_submit():
        flash(f'Get Your CV!', 'success')
        return redirect(url_for('home'))
    return render_template('workexp.html', form=form, x='workexp')
