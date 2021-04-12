"""Forms for site."""
from django import forms
from django.forms import ModelForm, Textarea, TextInput

from .models import Author, Post, Subscriber


class PostForm(ModelForm):
    """Postform class."""

    class Meta:
        """Meta class."""

        model = Post
        fields = ['title', 'description', 'content']
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название статьи"
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Описание статьи"
            }),
            "content": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Содержимое"
            })
        }


class SubscriberForm(ModelForm):
    """Subscriber Form."""

    author_id = forms.ModelChoiceField(
        queryset=Author.objects.all().order_by('name'),
        empty_label="Choose Author",
        widget=forms.Select(
            attrs={"class": "form-control"}
        )
    )

    class Meta:
        """Meta Сlass."""

        model = Subscriber
        fields = ['email_to', 'author_id']
        widgets = {
            "email_to": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Email подписчика "
            }),
        }
