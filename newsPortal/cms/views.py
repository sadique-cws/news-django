from django.shortcuts import render,redirect
from .models import Post,Category
# Create your views here.

from .forms import PostForm
def homepage(r):
    data = {}
    data['category'] = Category.objects.all()
    data['posts'] = Post.objects.all()
    return render(r,"home.html",data)


def insert(r):
    if r.method == "POST":
        p = PostForm(r.POST,r.FILES)
        if p.is_valid():
            p.save()
            return redirect(homepage)

    return render(r,"insert.html",{"form":PostForm})


def viewPost(r, cat_id):
    data = {}
    data['category'] = Category.objects.all()
    data['posts'] = Post.objects.filter(category=cat_id)
    return render(r, "home.html",data)


def singlePost(r,post_id):
    data = {}
    data['category'] = Category.objects.all()
    data['post'] = Post.objects.get(pk=post_id)
    data['posts'] = Post.objects.exclude(pk=post_id)
    return render(r, "view.html",data)

def search(r):
    search = r.GET.get("search")
    data = {
        "category":Category.objects.all(), 
        "posts":Post.objects.filter(title__contains=search)
        }
    return render(r, "home.html",data)