"""Users Views """

#Django
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#forms
from .forms import ProfileForm, SignUpForm
def login_view(request):
    """login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request,'users/login.html',{'error':'Invalid Username and Password'})

    return render(request, 'users/login.html')


def signup_view(request):
    """Singup View"""

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            return redirect('login')
    else:
        form = SignUpForm()
    return render(
        request=request, 
        template_name='users/signup.html',
        context={
            'form':form
        }
    )

@login_required
def update_profile(request):
    """update users profile view"""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data  =form.cleaned_data

            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.picture = data['picture']
            profile.save()
            
            return redirect('update_profile')
    else:
        form = ProfileForm()
     
    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile':profile,
            'user': request.user,
            'form':form,
        }
    )

@login_required
def logout_view(request):
    """logout view"""
    logout(request)
    return redirect('login')
