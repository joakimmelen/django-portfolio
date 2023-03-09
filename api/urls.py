from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("blog/posts/", views.blog_posts, name="blog_posts_api"),
]
