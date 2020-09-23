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


urlpatterns = [
    path('admin/',admin.site.urls),
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sort_integers),
    path('say_hi/<str:name>/<int:age>/',local_views.say_hi),
    path('posts/',post_views.list_posts)
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
