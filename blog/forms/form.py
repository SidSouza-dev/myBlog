from django import forms
from blog.models.post import Post
from django.core.exceptions import ValidationError
import re

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =  ['title', 'content']

    def clean_content(self):
        content = self.cleaned_data.get('content', '')
        if re.search(r'<script.*?>', content, re.IGNORECASE):
            raise ValidationError("Conteúdo não pode conter scripts.")
        return content