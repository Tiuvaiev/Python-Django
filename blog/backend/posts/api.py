from django.core import serializers
from django.http import JsonResponse

from .models import Post
from .serializers import PostSerializer


def posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    return JsonResponse({"results": serializer.data})


def post_detail(request, post_id: int):
    post = Post.objects.get(id=2)
    serializer = PostSerializer(post)

    return JsonResponse(serializer.data)
