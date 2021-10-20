from django.urls import path
from .views import HomeView, ArticleDetailView, NewPost, EditPostView, DeletePostView, NewCatagory, catagory,catagory_list
#Creating Urls
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article_details'),
    path('newpost',NewPost.as_view(),name = 'new_post'),
    path('article/edit/<int:pk>',EditPostView.as_view(),name = 'edit_post'),
    path('article/delete/<int:pk>',DeletePostView.as_view(),name = 'delete_post'),
    path('addcatagory',NewCatagory.as_view(),name = 'add_catagory'),
    path('catagory/<str:cats>',catagory,name='catagory_view'),
    path('catagories',catagory_list,name='catagory_list'),
]