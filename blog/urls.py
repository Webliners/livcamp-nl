from django.urls import path
from . import views
from .views import BlogView, ArticleView

urlpatterns = [
    path('', views.base_view, name='base'),
    #path('blog/', views.blog_overview, name='overview'),
    #path('blogpost/', views.blogpost_view, name='blogpost'),
    path('camperblog/', BlogView.as_view(), name='camperblog'),
    #path('article/<int:pk>', ArticleView.as_view(), name='blogpost'),
    path('<slug:slug>', ArticleView.as_view(), name='blogpost'),
    path('archive/', views.blogarchive_view, name='archive'),
]