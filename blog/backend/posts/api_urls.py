from django.urls import path

from posts.api import post_detail, posts

app_name = "posts_api"

urlpatterns = [
    path("posts/", posts, name="posts"),
    path(
        "posts/<int:post_id>/",
        post_detail,
        name="post_detail",
    ),
]
