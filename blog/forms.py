from django import forms

from .models import Post


class PostForm(forms.ModelForm): 
    class Meta:
        model = Post
        
        ### 3 states
        
        # fields = '__all__' # for all fields
        
        # fields = ['title', 'content', ]  # specific fields
        
        
        # Hind : that is a tuble ('test' , )
        exclude = ('author', ) # all except author
        