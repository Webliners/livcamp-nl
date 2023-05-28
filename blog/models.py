from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    title_tag = models.CharField(max_length=255, default='Livcamp')
    meta_tag = models.CharField(max_length=255, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    category = models.CharField(max_length=255, default='Algemeen', blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/") 

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("blogpost", kwargs={"slug: self.slug"})
