from django import forms
from .models import Document


class UploadForm(forms.Form):
    description = forms.CharField(max_length=225)
    document = forms.FileField()


class DocumentModelWithFileField(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['description', 'document']


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_email = forms.CharField(label='Your email', max_length=100)
    your_gender = forms.CharField(label='Your gender', max_length=100)
    your_school = forms.CharField(label='Your school', max_length=100)
    your_age = forms.CharField(label='Your age', max_length=100)
