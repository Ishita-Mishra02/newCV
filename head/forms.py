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
	email= StringField('Email',
						validators=[DataRequired(), Email()], render_kw={"placeholder": "123@email.com"})
	phone = StringField('Phone', validators=[DataRequired()])

	profession= StringField('Profession', validators=[DataRequired(), Length(min=2, max=25)], render_kw={"placeholder": "Profession"})
	city= StringField('City', validators=[DataRequired(), Length(min=2, max=25)])
	state= StringField('State', validators=[DataRequired(), Length(min=2, max=25)])
	zip= StringField('Zip', validators=[DataRequired(), Length(min=2, max=25)])
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
	c10 = StringField('Matric School', validators=[DataRequired(), Length(min=2,max=70)])
	g10= DecimalField('Percentage', validators=[DataRequired()])
	y10= IntegerField('Year of completion',validators=[DataRequired()])

	c12 = StringField('Post Matric School', validators=[DataRequired(), Length(min=2,max=70)])
	g12= DecimalField('Percentage', validators=[DataRequired()])
	y12= IntegerField('Year of completion',validators=[DataRequired()])

	pg = StringField('Institute')
	gpg= DecimalField('CGPA')
	ypg= IntegerField('Year of completion')

	g = StringField('Institute')
	gg= DecimalField('CGPA')
	yg= IntegerField('Year of completion')
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
