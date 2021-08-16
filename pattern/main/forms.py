from django import forms
from .models import Post

class PostData(forms.Form):
	class meta:
		model = Post
		fields = '__all__'