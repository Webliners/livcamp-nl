from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.

#Base View
#def base_view(request):
#    return render(request, 'base.html')

class BaseView(TemplateView):
    model = Post
    template_name = 'base.html'

#Blog Overview
#def blog_overview(request):
#    return render(request, 'overview.html')

class BlogView(ListView):
    model = Post
    template_name = 'camperblog.html'
    # ordering = ['-id']

#BlogPost
#def blogpost_view(request):
#    return render(request, 'blogpost.html')
class ArticleView(DetailView):
    model = Post
    template_name = 'blogpost.html'

#BlogArchive
def blogarchive_view(request):
    return render(request, 'archive.html')

#AddPost
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

#UpdatePost
class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    #fields = '__all__'

#DeleteView
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('camperblog')

#Themalijsten
