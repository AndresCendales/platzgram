"""
platzigram URL Configuration
"""
#Django
from django.contrib import admin
from django.urls import path
from platzigram import views as local_views
from django.conf.urls.static import static
from django.conf import settings

#Views from posts
from posts import views as post_views

#Views from users
from users import views as users_views


urlpatterns = [
    path('admin/',admin.site.urls),
    path('hello-world/', local_views.hello_world, name='Hello_World'),
    path('sorted/', local_views.sort_integers, name='sort'),
    path('say_hi/<str:name>/<int:age>/',local_views.say_hi, name='hi'),
    
    path('',post_views.list_posts,name='feed'),
    path('/posts/new/',post_views.create_post,name='create_post'),
    
    
    path('users/login/', users_views.login_view,name='login'),
    path('users/logout/', users_views.logout_view,name='logout'),
    path('users/signup/', users_views.signup_view,name='signup'),
    path('users/me/profile/', users_views.update_profile,name='update_profile'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
