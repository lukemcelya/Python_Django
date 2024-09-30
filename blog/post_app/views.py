from django.shortcuts import render
from post_app.models import BlogPost

# Create your views here.
def posts(request):
    blog_posts = BlogPost.objects.all()
    posts_dictionary = {'post_key' : blog_posts}
    return render(request, 'posts.html', context=posts_dictionary)