from django.shortcuts import render

# Create your views here.


def homepage(r):
    return render(r,"home.html")


def insert(r):
    if r.method == "POST":
        pass 
    return render(r,"insert.html")

