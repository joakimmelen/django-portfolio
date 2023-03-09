from django.http import JsonResponse
from django.core import serializers
from blog.models import Post


def blog_posts(request):
    # Retrieve all blog posts from the database
    posts = Post.objects.all()

    # Serialize the posts to JSON
    data = serializers.serialize("json", posts)

    # Return the data as a JSON response
    return JsonResponse(data, safe=False)
