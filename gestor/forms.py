# gestor/forms.py
from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['case','file']  # Campo del archivo para drag & drop
