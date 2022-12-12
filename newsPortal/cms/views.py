from django.shortcuts import render
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
        pass 
    return render(r,"insert.html",{"form":PostForm})

