from django.urls import path
from . import views
from .views import BlogView, ArticleView, BaseView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    #path('blog/', views.blog_overview, name='overview'),
    #path('blogpost/', views.blogpost_view, name='blogpost'),
    path('camperblog/', BlogView.as_view(), name='camperblog'),
    #path('article/<int:pk>', ArticleView.as_view(), name='blogpost'),
    path('<slug:slug>', ArticleView.as_view(), name='blogpost'),
    path('archive/', views.blogarchive_view, name='archive'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('edit/<slug:slug>', UpdatePostView.as_view(), name='update_post'),
    path('<slug:slug>/delete', DeletePostView.as_view(), name='delete_post'),
]