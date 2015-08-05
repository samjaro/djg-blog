from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from .models import Places

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def vitoria(request):
    places = Places.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/vitoria.html', {'places': places})



#def vitoria_detail(request):
 #   place = get_object_or_404(Places, pk=pk)
  #  return render(request, 'blog/vitoria_detail.html', {'place': place})

def florida(request):
    places = Places.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/florida.html', {'places': places})

def santa_maria(request):
    places = Places.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/santa_maria.html', {'places': places})  

def cuesta(request):
    places = Places.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/cuesta.html', {'places': places})    

def contact(request):
    return render(request, 'blog/contact.html')   