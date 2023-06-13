from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, default='Livcamp')
    updated = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title