from app.models import *
from django import forms

class Topicform(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
class Webpageforms(forms.ModelForm):
    class Meta:
        model = Webpage
        fields = '__all__'

