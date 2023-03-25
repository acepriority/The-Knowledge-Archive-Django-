from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your forms here.

class NewUserForm(UserCreationForm):
	student_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'input','placeholder':'Student Number'}))

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2","student_number"]

	def __init__(self, *args, **kwargs):
		super(NewUserForm,self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'input'
		self.fields['username'].widget.attrs['placeholder'] = 'Username'
		self.fields['email'].widget.attrs['class'] = 'input'
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['password1'].widget.attrs['class'] = 'input'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password2'].widget.attrs['class'] = 'input'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

