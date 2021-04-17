from django.db import models
from django.utils.text import slugify
# Create your models here.
from django.contrib.auth.models import User

import misaka
from django.urls import reverse
from django.utils import timezone
from django import template
register = template.Library()

class Usergroup(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True,unique = True)
    description = models.TextField(null = True,default = '')
    description_html = models.TextField(editable=False,null = True,default = '')
    created_at = models.DateTimeField(default=timezone.now())
#    groupadmin = models.ForeignKey(User,related_name='project',on_delete=models.CASCADE)
    users = models.ManyToManyField(User,through='GroupMember')



    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('usergroups:single',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Usergroup,related_name='members',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='members',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


    class Meta:
        unique_together = ['group','user']
