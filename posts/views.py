"""Posts for platzigram"""
#django
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

#Django Auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#forms 
from .forms import PostForm

#utilities
from datetime import datetime


#Models
from .models import Post

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""
    template_name='posts/feed.html'
    model = Post
    ordering = '-created'
    paginate_by = 30
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin,DetailView):
    """ Return post detail"""
    template_name='posts/detail.html'
    quesyset = Post.objects.all()
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin,CreateView):
    """create a new post."""
    template_name='posts/new.html'
    form_class= PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """add user and profile to the context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        
        return context