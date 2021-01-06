from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import BlogPost,Category



def index(request):
    posts = BlogPost.objects.all()
    cats = Category.objects.all()

    if 'category' in request.GET:
        posts = posts.filter(category = int(request.GET.get('category')))

    if 'postid' in request.GET:
        posts = posts.filter(id = int(request.GET.get('postid')))

    context = {
        'posts' : posts.order_by('-created_at'),
        'cats' : cats
    }
    return render(request,'index.html',context)

def view_post(request):
    post = BlogPost.objects.get(pk=int(request.GET.get('postid')))
    cats = Category.objects.all()
    return render(request,'post.html',{'post':post,'cats' : cats})




