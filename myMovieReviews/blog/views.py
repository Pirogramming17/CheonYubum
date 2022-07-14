from django.shortcuts import render, redirect
from multiprocessing import context
from django.utils import timezone
from .models import Blog

# Create your views here.
def listpage(request):
    posts = Blog.objects.filter(updated_at__lte=timezone.now()).order_by('updated_at')
    context = {
        "posts":posts
    }
    return render(request, template_name='blog/listpage.html', context=context)

def detail(request, id):
    post = Blog.objects.get(id=id)
    context = {
        "post":post
    }
    return render(request, template_name='blog/detail.html', context=context)

def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        comeout = request.POST["comeout"]
        genre = request.POST["genre"]
        score = request.POST["score"]
        runnintime = request.POST["runnintime"]
        review = request.POST["review"]
        direct = request.POST["direct"]
        maincha = request.POST["maincha"]

        Blog.objects.create(title=title, comeout=comeout, genre=genre, score=score, runnintime=runnintime, review=review, direct=direct, maincha=maincha)

        return redirect('/')
    
    context = {}

    return render(request, template_name="blog/create.html", context=context)

def update(request, id):
    if request.method == "POST":
        title = request.POST["title"]
        comeout = request.POST["comeout"]
        genre = request.POST["genre"]
        score = request.POST["score"]
        runnintime = request.POST["runnintime"]
        review = request.POST["review"]
        direct = request.POST["direct"]
        maincha = request.POST["maincha"]

        Blog.objects.filter(id=id).update(title=title, comeout=comeout, genre=genre, score=score, runnintime=runnintime, review=review, direct=direct, maincha=maincha)
        return redirect(f"/post/{id}")
    
    post = Blog.objects.get(id=id)
    context = {
        "post":post
    }

    return render(request, template_name='blog/update.html', context=context)

def delete(request, id):
    if request.method == "POST":
        Blog.objects.filter(id=id).delete()
        return redirect('/')

