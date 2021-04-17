from django.db import models
from django.utils.text import slugify
# Create your models here.
from django.contrib.auth.models import User

import misaka
from django.urls import reverse
from django.utils import timezone
from django import template
from usergroups.models import Usergroup
register = template.Library()

class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True,unique = True)
    description = models.TextField(null = True,default = '')
    description_html = models.TextField(editable=False,null = True,default = '')
    created_at = models.DateTimeField(default=timezone.now())
    owner = models.ForeignKey(User,related_name='project',on_delete=models.CASCADE)
    completed_at = models.DateTimeField(blank=True,null=True)
    group = models.ForeignKey(Usergroup,related_name='projects',null=True,blank=True,on_delete=models.CASCADE)



    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('projects:single',kwargs={'slug':self.slug})


class Comment(models.Model):
    author = models.ForeignKey(User,related_name = 'comments',on_delete=models.CASCADE)
    text = models.TextField()
    text_html = models.TextField(editable=False,null = True,default = '')
    project = models.ForeignKey(Project,related_name = 'comments',on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
            return reverse('projects:all')

    def __str__(self):
            return self.text

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.text_html = misaka.html(self.text)
        super().save(*args,**kwargs)
