from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

from .models import Post, Comment

# Apply summernote to all TextField in model.
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    
    list_display = ['title', 'draft', 'author']
    
    list_filter = ['author', 'draft']
    
    search_fields = ['title']
    

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'create_date']
    
    




admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)    