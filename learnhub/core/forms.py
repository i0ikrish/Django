from django import forms
from .models import Note
from .models import Document


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Note title"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Write your note..."}),
        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']
