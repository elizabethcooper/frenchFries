from django import forms


class RegisterForm(forms.Form):
	username = forms.CharField(max_length=1000)
	name = forms.CharField(max_length=1000)
	email = forms.CharField(max_length=1000)
	image = forms.FileField()
