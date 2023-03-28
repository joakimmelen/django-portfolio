from django.core.serializers import serialize
from django.http import JsonResponse
from django.db.models import Prefetch
from blog.models import Post, Comment, Tag
import json


def serialize_post(post):
    return {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "author": {"id": post.author.id, "username": post.author.username},
        "created_at": post.created_at,
        "updated_at": post.updated_at,
        "image": post.image.url if post.image else None,
        "tags": [tag.id for tag in post.tags.all()],
    }


def serialize_comment(comment):
    return {
        "id": comment.id,
        "postId": comment.post.id,
        "content": comment.content,
        "author": {"id": comment.author.id, "username": comment.author.username},
    }


def serialize_tag(tag):
    return {
        "id": tag.pk,
        "name": tag.name,
    }


def blog_posts(request):
    posts = Post.objects.prefetch_related(Prefetch("tags", queryset=Tag.objects.all()))

    post_data = [serialize_post(post) for post in posts]

    comments = Comment.objects.all()
    comment_data = [serialize_comment(comment) for comment in comments]

    tags = Tag.objects.all()
    tag_data = [serialize_tag(tag) for tag in tags]

    return JsonResponse(
        {
            "posts": post_data,
            "comments": comment_data,
            "tags": tag_data,
        }
    )
