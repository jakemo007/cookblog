from django import forms
from .models import Post,Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','title_tag','author','category','body']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control','placeholder':'cooking'}),
            'author': forms.TextInput(attrs={'class' : 'form-control','type':'hidden','value':'', 'id':'username'}),
            'category':forms.Select(choices= [item for item in Category.objects.all().values_list('name','name')],attrs={'class' : 'form-control'}),
            'body'  : forms.Textarea(attrs={'class' : 'form-control'}),
        }

class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','title_tag','category','body']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control','placeholder':'cooking'}),
            'category':forms.Select(choices= [item for item in Category.objects.all().values_list('name','name')],attrs={'class' : 'form-control'}),
            'body'  : forms.Textarea(attrs={'class' : 'form-control'}),
        }


        