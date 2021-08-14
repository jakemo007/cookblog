from django.urls import path
from .views import HomeView, ArticleDetailView, NewPost, EditPostView, DeletePostView

#Creating Urls
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article_details'),
    path('newpost',NewPost.as_view(),name = 'new_post'),
    path('article/edit/<int:pk>',EditPostView.as_view(),name = 'edit_post'),
    path('article/delete/<int:pk>',DeletePostView.as_view(),name = 'delete_post'),
]