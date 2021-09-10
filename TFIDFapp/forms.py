from django import forms
from TFIDFapp.models import AddFile
import os
from TFIDF.settings import MEDIA_ROOT


class UploadFileForm(forms.ModelForm):
    '''Форма для добавления файла'''
    class Meta:
        model = AddFile
        fields = ['file']


class ComputeForm(forms.Form):
    '''Форма для указания номера документа, относительно которого необходимо посчитать TF'''
    doc_number = forms.IntegerField(max_value=len(os.listdir(MEDIA_ROOT + "/files/")))
