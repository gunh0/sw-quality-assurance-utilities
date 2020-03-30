from django import forms
from django.forms import ModelForm
from .models import Testreserve
from django.forms.fields import DateTimeField

class ReserveForm(forms.ModelForm):
	class Meta:
		model = Testreserve
		fields = ['name', 'project', 'memo', 'starttime']