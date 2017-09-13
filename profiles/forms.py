from django.forms import ModelForm

from profiles.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['message', 'file']
