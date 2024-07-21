from django.shortcuts import render, get_object_or_404
from .models import Post
from packages.models import package

def post_list(request):
    posts = Post.objects.all().order_by("-created_date")
    print(posts)
    return render(request, 'blog/post_list.html', {"posts": posts})

def blog_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # packages which are isfeatured
    featured_packages = package.objects.filter(IsFeatured=True)
    other_posts = Post.objects.exclude(pk=pk).order_by("-created_date")
    print(other_posts[1])
    return render(request, 'blog/blog_details.html', {"post": post, "other_post": other_posts[1], "featured_packages": featured_packages[0:3]})
