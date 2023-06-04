from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.

#Base View
#def base_view(request):
#    return render(request, 'base.html')

class BaseView(ListView):
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
    
    #def get_context_data(self, *args, **kwargs):
       #category_menu = Category.objects.all()
       #context = super(ArticleView, self).get_context_data(*args, **kwargs)

       #stuff = get_object_or_404(Post, slug=self.kwargs(['slug']))
      # total_likes = stuff.total_likes()
      # context["category_menu"] = category_menu
      # context["total_likes"] = total_likes
      ## return context
    

#BlogArchive
def blogarchive_view(request):
    return render(request, 'archive.html')

#AddPost
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

#AddCategory
class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'   

#Category Overview
class CategoryOverView(ListView):
    model = Post
    template_name = 'categoriesoverview.html'
    cats = Category.objects.all()

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(CategoryOverView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


#Catogrie bekijken
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})

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

#Likes
#def LikeView(request, slug):
 #   post = get_object_or_404(Post, id=request.POST.get('post_id'))
 #   post.likes.add(request.user)
 #   return HttpResponseRedirect(reverse('blogpost', args=[str(slug)]))

#Themalijsten
