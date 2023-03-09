from django.core.serializers import serialize
from django.http import JsonResponse

from blog.models import Post, Comment, Tag


def blog_posts(request):
    posts = Post.objects.all()
    post_data = serialize("json", posts)

    comments = Comment.objects.all()
    comment_data = serialize("json", comments)

    tags = Tag.objects.all()
    tag_data = serialize("json", tags)

    return JsonResponse(
        {
            "posts": post_data,
            "comments": comment_data,
            "tags": tag_data,
        }
    )
