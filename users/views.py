"""Users Views """

#Django
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView

#forms
from .forms import SignUpForm

#Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

class UserDetailView(LoginRequiredMixin,DetailView):
    """user detail view"""
    template_name = 'users/detail.html'
    slug_field='username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """add users posts to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context
    

def login_view(request):
    """login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            return redirect('posts:feed')
        else:
            return render(request,'users/login.html',{'error':'Invalid Username and Password'})

    return render(request, 'users/login.html')



class SignUpView(FormView):
    """users signup view"""
    template_name = 'users/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')

    def form_valid(self,form):
        """save form data"""
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile of user"""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website','biography','phone_number','picture']

    def get_object(self):
        """return users profile"""
        return self.request.user.profile

    def get_success_url(self):
        """return to user's profile"""
        username = self.object.user.username
        return reverse('users:detail',kwargs={'username':username})


@login_required
def logout_view(request):
    """logout view"""
    logout(request)
    return redirect('users:login')
