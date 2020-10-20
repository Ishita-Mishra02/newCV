from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange

class RegistrationForm(FlaskForm):
	username=StringField('Username',
						  validators=[DataRequired(), Length(min=2, max=25)], render_kw={"placeholder": "Username"})
	email= StringField('Email',
						validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
	password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
	confirm_password=PasswordField('Confirm Paasword',
									validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
	submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
	email= StringField('Email',
						validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
	password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login In')

class details(FlaskForm):   #basic details
	firstname= StringField('First Name', validators=[DataRequired(), Length(min=2, max=25)])
	lastname= StringField('Last Name', validators=[DataRequired(), Length(min=2, max=25)])

	phone = StringField('Phone', validators=[DataRequired()])

	profession= StringField('Profession', validators=[DataRequired(), Length(min=2, max=25)])
	city= StringField('E-mail(to be written on CV)', validators=[DataRequired(), Length(min=2, max=25)])
	state= StringField('State', validators=[DataRequired(), Length(min=2, max=25)])
	submit= SubmitField('Next')

class skills(FlaskForm):    #skills+aoi+hobbies
	s1= StringField('skill-1', validators=[DataRequired(), Length(min=2, max=25)])
	s2= StringField('skill-2', validators=[Length(min=2, max=25)])
	s3= StringField('skill-3', validators=[Length(min=2, max=25)])

	a1= StringField('Area of Interest-1', validators=[DataRequired(), Length(min=2, max=25)])
	a2= StringField('Area of Interest-2', validators=[Length(min=2, max=25)])
	a3= StringField('Area of Interest-3', validators=[Length(min=2, max=25)])

	h1= StringField('Hobby-1', validators=[DataRequired(), Length(min=2, max=25)])
	h2= StringField('Hobby-2', validators=[Length(min=2, max=25)])
	h3= StringField('Hobby-3', validators=[Length(min=2, max=25)])

	submit= SubmitField('Next')

class education(FlaskForm): #school +college
	c10 = StringField('Class-10/ Matric School', validators=[DataRequired(), Length(min=2,max=70)])
	g10= DecimalField('Class-10 percentage', validators=[DataRequired()])
	y10= IntegerField('Year of completing Class-10',validators=[DataRequired()])

	c12 = StringField('Class-12/Post Matric School', validators=[DataRequired(), Length(min=2,max=70)])
	g12= DecimalField('Class-12 percentage', validators=[DataRequired()])
	y12= IntegerField('Year of completing Class-12',validators=[DataRequired()])

	pg = StringField('Post Graduation Institute')
	gpg= DecimalField('Post Graduation CGPA')
	ypg= IntegerField('Year of completing Post Graduation')

	g = StringField('Graduation Institute')
	gg= DecimalField('Graduation CGPA')
	yg= IntegerField('Year of completing Graduation')
	submit= SubmitField('Next')

class workhistory(FlaskForm):  #projects+work_exp
	p1= StringField('1 ')
	p2= StringField('2 ')
	p3= StringField('3 ')

	w1= StringField('1 ')
	w2= StringField('2 ')
	w3= StringField('3 ')

	o1= StringField('1 ')
	o2= StringField('2 ')
	o3= StringField('3 ')
	o4= StringField('4 ')
	submit= SubmitField('Next')
