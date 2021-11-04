"""
Post:
id: int +
title: str
content: str
author_id: int

User:
id: int
username: str
first_name: str
last_name: str
password: str
"""
from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE
    )

    # If we don't wanna use real delete from the database. Look into the view.py PostsListView
    # deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # def save(self, author):
    #     self.author = author
    #     instance = self.save()
    #     return super().save()


# me = User.objects.get(id=3)
# me.posts.all() <== Queryset()

# Post.objects.all() <== Queryset()
# Post.objects.first() <== Model
# Post.objects.last()
# Post.objects.create(author=admin, title='asdasd')
# Post.objects.update()
# post = Post.objects.get(author_id=3)
# result = Post.objects.filter(title="VIM")

# Что такое result ?
# result -> QuerySet() == list[dict,]
# post = Post.objects.first()

# results = [{}, {}, {}]
# post = results[2]
# post = {
# 	"id": 1,
# 	"title": "VIM"
# 	"content": "How to learn VIM",
# 	"author_id": 3
# }

# post["title"] ==> post.id / post.content
# ======================
# post = Post.objects.get(title="VIM")
# ??? post.author.username ???
# author = User.objects.get(id=post.author_id)
# author.username !!!!!!
