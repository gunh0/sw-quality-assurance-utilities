from django import forms
from django.forms import ModelForm
from .models import Performagent

class ReserveForm(forms.ModelForm):
	class Meta:
		model = Performagent
		fields = ['ostype', 'process1', 'process2', 'process3', 'process4', 'process5']