from django.urls import path
from . import views_blog

app_name = "api"

urlpatterns = [
    path("blog/posts/", views_blog.blog_posts, name="blog_posts_api"),
]
