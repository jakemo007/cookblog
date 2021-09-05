from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, PostEditForm
from django.urls import reverse_lazy


# Create your views here.
# def home(request):
#     return render(request,'home.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'articles_view.html'

class NewPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ['title','body']

class NewCatagory(CreateView):
    model = Category
    template_name = 'add_catagory.html'
    fields = '__all__'

class EditPostView(UpdateView):
    model = Post
    form_class = PostEditForm
    # fields = ['title','body']
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def catagory(request,cats):
    catagory = Post.objects.filter(category=cats)
    data = {'cats':cats,'catagory':catagory}
    return render(request,'catagory_view.html',data)
    


