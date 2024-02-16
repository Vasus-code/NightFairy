from django.forms import ModelForm

from .models import Db



class DbForm(ModelForm):
	class Meta:
		model = Db
		fields = ('title', 'content', 'price', 'rubric', 'img_name')