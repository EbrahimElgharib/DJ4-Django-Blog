from django.shortcuts import render, redirect

from .models import Post

from .forms import PostForm

# Create your views here.


def post_list(request):
    data = Post.objects.all()
    return render(request, 'post_list.html', context={'posts':data})


def post_detail(request, post_id):
    data = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', context={'post':data})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            
            # Without this next line the tags won't be saved.
            form.save_m2m()
            
            return redirect('/blog/')
        
    else:
        form = PostForm()
        
    return render(request, 'new_post.html', context={'form':form})




def  edit_post(request, post_id):
    data = Post.objects.get(id = post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            
            # Without this next line the tags won't be saved.
            form.save_m2m()
            
            return redirect('/blog/')
        
    else:
        form = PostForm(instance=data)
        
    return render(request, 'edit_post.html', context={'form':form})





def delete_post(request, post_id):
    data = Post.objects.get(id = post_id)
    
    data.delete()
    
    return redirect('/blog/')
    