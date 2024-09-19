from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def home(request):
    post_list = Post.objects.all()  # Get all blog posts
    paginator = Paginator(post_list, 5)  # Paginate, 5 posts per page
    page = request.GET.get('page')  # Get the current page number
    posts = paginator.get_page(page)  # Retrieve the posts for the current page
    return render(request, 'blog/home.html', {'posts': posts})  # Render template with paginated posts