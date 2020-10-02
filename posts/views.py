"""Posts for platzigram"""
#django
from django.shortcuts import render, redirect #recibe un request,template y contexto
from django.http import HttpResponse

#Django Auth
from django.contrib.auth.decorators import login_required

#forms 
from .forms import PostForm

#utilities
from datetime import datetime


#Models
from .models import Post


@login_required
def list_posts(request):
    """List existing posts."""
    posts = Post.objects.all().order_by('-created')

    return render(request, 'posts/feed.html', {'posts': posts})



@login_required
def create_post(request):
    """create new post"""
    if request.method == 'POST':
        form= PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form':form,
            'user':request.user,
            'profile': request.user.profile,
        },
    )