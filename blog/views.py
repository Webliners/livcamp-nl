from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post

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

#BlogPost
#def blogpost_view(request):
#    return render(request, 'blogpost.html')
class ArticleView(DetailView):
    model = Post
    template_name = 'blogpost.html'

#BlogArchive
def blogarchive_view(request):
    return render(request, 'archive.html')

#Themalijsten
