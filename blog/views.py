from django.shortcuts import render, redirect

from .models import Post, Comment

from .forms import PostForm, CommentForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.


# def post_list(request):
#     data = Post.objects.all()
#     return render(request, 'post_list.html', context={'posts':data})


class PostList(ListView):
    model = Post
    
    



def post_detail(request, pk):
    data = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=data)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.post = data
            myform.save()
    
    # else:
    form = CommentForm()
        
    return render(request, 'blog/post_detail.html', context={'post':data, 'form':form, 'comments':comments})


# class PostDetail(DetailView):
#     model = Post
    

# def post_new(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             myform = form.save(commit=False)
#             myform.author = request.user
#             myform.save()
            
#             # Without this next line the tags won't be saved.
#             form.save_m2m()
            
#             return redirect('/blog/')
        
#     else:
#         form = PostForm()
        
#     return render(request, 'new_post.html', context={'form':form})

class PostCreate(UpdateView):
    model = Post
    
    fields = ['title', 'content', 'image', 'tags', 'create_date', 'draft', 'author']
    
    success_url = '/blog'
    




# def  edit_post(request, post_id):
#     data = Post.objects.get(id = post_id)
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=data)
#         if form.is_valid():
#             myform = form.save(commit=False)
#             myform.author = request.user
#             myform.save()
            
#             # Without this next line the tags won't be saved.
#             form.save_m2m()
            
#             return redirect('/blog/')
        
#     else:
#         form = PostForm(instance=data)
        
#     return render(request, 'edit_post.html', context={'form':form})


class PostUpdate(UpdateView):
    model = Post
    
    fields = ['title', 'content', 'image', 'tags', 'create_date', 'draft', 'author']
    
    success_url = '/blog'
    
    template_name = 'blog/edit_post.html'


# def delete_post(request, post_id):
#     data = Post.objects.get(id = post_id)
    
#     data.delete()
    
#     return redirect('/blog/')
    
class PostDelete(DeleteView):
    model = Post
        
    success_url = '/blog'
