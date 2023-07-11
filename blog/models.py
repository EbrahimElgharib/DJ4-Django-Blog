from django.db import models

from django.utils import timezone

from taggit.managers import TaggableManager

from django.contrib.auth.models import User


'''
    features
    - fields, options
    - flexible with different Database
    - validation
    - html widget
'''

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=30000)
    create_date = models.DateTimeField(default=timezone.now)
    
    draft = models.BooleanField(default=True)

    tags = TaggableManager()
    
    author = models.ForeignKey(User, related_name='post_user', null=True, on_delete=models.SET_NULL)