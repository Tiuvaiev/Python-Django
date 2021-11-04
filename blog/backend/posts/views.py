# from django.http import HttpRequest, HttpResponse
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import PostCreateForm
from .models import Post

User = get_user_model()


# def posts(request: HttpRequest) -> HttpResponse:
#     qs = Post.objects.all()
#     post_titles = [post.title for post in qs]
#
#     content = f"""<h1>Posts: {post_titles}</h1>"""
#
#     return HttpResponse(content)


class PostsListView(ListView):
    model = Post
    template_name = "posts/index.html"
    authentication_classes = []

    def get(self, request):
        return super().get(request)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        ctx["foo"] = 12

        return ctx

    def get_queryset(self):
        # See in the model.
        # return Post.objects.filter(deleted=False)
        if isinstance(self.request.user, User):
            return Post.objects.filter(author=self.request.user)
        return None


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
    context_object_name = "my_post"


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy("posts:list")
    template_name = "posts/create.html"
    # fields = ["title", "content"] # Uses only with model (not with form_class)

    # def post(self, request):
    #     user = request.user

    #     return super().post(request)

    # def form_valid(self, form):
    #     self.object = form.save(author=self.request.user)
    #     return super().form_valid(form)

    # Better approach in the forms.py file
    def post(self, request):
        data = dict(request.POST)
        form = PostCreateForm(data)
        if form.is_valid():
            form.cleaned_data["author"] = request.user
            Post.objects.create(**form.cleaned_data)

        return HttpResponseRedirect(reverse_lazy("posts:list"))


class PostUpdateView(UpdateView):
    model = Post
    success_url = reverse_lazy("posts:list")
    template_name = "posts/update.html"
    fields = ["title", "content"]


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("posts:list")
    template_name = "posts/delete.html"

    # Use if we don't wanna use real delete from the database. Look into the models.py :: Post
    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     self.object.deleted = True
    #     self.object.save()

    #     return HttpResponseRedirect(success_url)
