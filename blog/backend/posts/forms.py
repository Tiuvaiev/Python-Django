from django.contrib.auth import get_user_model
from django import forms

from .models import Post

User = get_user_model()


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

    # def save(self, author: User):
    #     self.instance.author = author
    #     self.instance.save()
    #     return self.instance

