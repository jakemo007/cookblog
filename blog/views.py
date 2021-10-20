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

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'articles_view.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView,self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

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
    catagory = Post.objects.filter(category=cats.title().replace('-',' '))
    return render(request,'catagory_view.html',{'cats':cats.title().replace('-',' '),'catagory':catagory})

def catagory_list(request,*args,**kwargs):
    catagory = Category.objects.all()
    return render(request,'catagory_list.html',{'catagory_list':catagory})
    


