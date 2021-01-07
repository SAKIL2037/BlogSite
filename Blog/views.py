from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage

# Create your views here.
from .models import BlogPost,Category



def index(request):
    posts = BlogPost.objects.all()
    cats = Category.objects.all()

    if 'category' in request.GET:
        page = posts.filter(category = int(request.GET.get('category')))
        pageNumber = 1
    elif 'postid' in request.GET:
        page = posts.filter(id = int(request.GET.get('postid')))

    elif 'post' not in request.GET:
        posts = Paginator(posts, 5)
        pageNumber = request.GET.get('page', 1)
        try:
            page = posts.page(pageNumber)
        except EmptyPage:
            page = posts.page(pageNumber)
    context = {
        'posts': page,
        'cats': cats,
        'pn': pageNumber
    }
    return render(request, 'index.html', context)



def category(request):

    return render(request,'category.html')



def view_post(request):
    post = BlogPost.objects.get(pk=int(request.GET.get('postid')))
    cats = Category.objects.all()
    return render(request,'post.html',{'post':post,'cats' : cats})




