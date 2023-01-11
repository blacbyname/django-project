from django import forms

from .models import Article

class AricleForm(forms.ModelForm):
    class Meta :
        model = Article
        fields = [
            'title',
            'summary',
            'article',
        ]
