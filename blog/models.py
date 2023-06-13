from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("add_category")
        

class Profile(models.Model):
    #associoation to Usermodel model (members)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/") 
    website_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    youtube_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)

    #to see it in admin
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse("base")
        

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    title_tag = models.CharField(max_length=255, default='Livcamp')
    meta_tag = models.CharField(max_length=255, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    category = models.CharField(max_length=255, default='Algemeen', blank=True, null=True)
    snippet = models.CharField(max_length=255, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/") 
    updated = models.DateField(null=True, blank=True)
    #likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        #return reverse("blogpost", kwargs={"slug: self.slug"})
        return reverse("blogpost", kwargs={'slug': self.slug})
        #return reverse("blogpost", args=(str(self.slug)))

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

