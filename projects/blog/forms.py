from django import forms
from .models import Post, Comment 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

User = get_user_model()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text','category','tag','image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',) 

class EditProfileForm(UserChangeForm):
    class Meta:
        model=User
        fields=('username','email')        
