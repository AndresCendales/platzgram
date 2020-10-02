"""Forms for posts """

#Django models
from .models import Post

#Forms
from django import forms


class PostForm(forms.ModelForm):
    """Post model form."""

    class Meta:
        """Form settings"""
        model = Post
        fields = ('user','profile','title', 'photo')