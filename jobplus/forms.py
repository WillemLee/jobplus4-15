from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Length,Email,EqualTo,Required

#class RegisterForm(FlaskForm):
#	username = StringField('',validators=[Required(),Length(3,24)])
#	email = StringField('',validators=[Required(),Email()])
#	password = PasswordField('',validators=[Required(),Length(6,24)])
# 	repeat_password = PasswordField('',validators=[Required(),EqualTo('password')])

class LoginForm():
	email = StringField('邮箱',validators=[Required(),Email()])
	password = PasswordField('密码',validators=[Required(),Length(6,24)])
	remember_me = BooleanField('记住我')
	submit = SubmitField('提交')