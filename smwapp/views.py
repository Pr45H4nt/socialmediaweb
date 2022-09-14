from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import *
from django.db.models import Q
from random import shuffle

def registerpage(request):
    f = RegisterForm()
    if request.method == "POST":
        f = RegisterForm(request.POST)
        if f.is_valid():
            f.save()
            new_user = authenticate(username=f.cleaned_data['username'],
                                    password=f.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect("home")
        else:
            print(f.errors)
        
    data = {
        'form' : f
    }
    return render(request, "registerpage.html" , data)


def loginpage(request):
    f = loginForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            print('invalid credentials')
    data = {
        'form' : f
    }
    return render(request, "login.html", data)

def logoutpage(request):
    logout(request)
    return redirect("loginpage")

@login_required(login_url='loginpage')
def home_view(request):
    items = post.objects.all()
    qwery = request.GET.get('qwery')
    if qwery != None:
        items= post.objects.filter(status__icontains = qwery)
    items = list(items)
    shuffle(items)

    data = {
        'posts' : items
    }
    return render(request, "home.html", data)

@login_required(login_url='loginpage')
def addpostview(request):
    form = postform()
    if request.method == "POST":
        form = postform(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("home")
    data = {
        'form' : form
    }
    return render(request, "addpost.html",data)

@login_required(login_url='loginpage')
def specific_post(request, slug):
    reply = replyform()
    obj = post.objects.get(slug = slug)
    form = commentform()
    if request.method == "POST":
        form = commentform(request.POST)
        if form.is_valid():
            q = form.save(commit=False)
            q.user = request.user
            q.post = obj
            q.save()
    comments = obj.comments_set.all()

    try:
        like_obj = likes.objects.get(Q(post=obj) & Q(user = request.user))
        a = like_obj.has_liked
    except:
        a = False
    data =  {
        'post' : obj,
        'comments' : comments ,
        'liked' : a ,
        'form' : form ,
        'rform' : reply
    }
    return render(request, "specpost.html", data)


@login_required(login_url='loginpage')
def likedview(request, slug):
    obj = post.objects.get(slug=slug)
    try:
        like_obj = likes.objects.get(Q(post=obj) & Q(user = request.user))
        if like_obj.has_liked == True:
            like_obj.has_liked = False
            like_obj.save()
            obj.no_of_likes -= 1
            obj.save()
        else:
            like_obj.has_liked = True
            like_obj.save()
            obj.no_of_likes += 1
            obj.save()
    except:
        like_obj= likes(user=request.user , post = obj , has_liked=True)
        like_obj.save()
        obj.no_of_likes += 1
        obj.save()
        
    return redirect('post',slug = obj.slug)


@login_required(login_url='loginpage')
def editpost(request, slug):
    obj = post.objects.get(slug = slug)
    form = postform(initial={'status' : obj.status})
    if request.method == "POST":
        form = postform(request.POST)
        if form.is_valid():
            q = form.cleaned_data['status']
            obj.status = q
            obj.save()
            return redirect("home")
    return render(request, "editpost.html", {'form':form})


@login_required(login_url='loginpage')
def deletepost(request, slug):
    obj = post.objects.get(slug=slug)
    obj.delete()
    return redirect("home")


@login_required(login_url="loginpage")
def deletecomment(request, id):
    comment = comments.objects.get(id=id)
    p = comment.post.slug
    comment.delete()
    return redirect("post" , slug = p)


@login_required(login_url='loginpage')
def mytweets(request):
    items = post.objects.all()
    items = items.filter(user=request.user)
    data = {
        'posts' : items
    }
    return render(request, "home.html", data)