from django import forms
from .models import Todo

class todo_form(forms.ModelForm):
    class Meta:
        model = Todo

        fields = [
            "title",
            "desc"]