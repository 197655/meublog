from django import forms
from .models import Postagem

class PostForm(forms.ModelForm):
	"""docstring for PostForm"""
	class Meta:
		model = Postagem
		fields = ('titulo', 'texto')