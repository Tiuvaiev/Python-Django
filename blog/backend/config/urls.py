from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponseRedirect
from django.urls import include, path


def redirect_to_posts(request):
    return HttpResponseRedirect("posts/")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", redirect_to_posts),
    path("posts/", include("posts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),

    path("api/", include("posts.api_urls")),
    # path("accounts/", include('accounts.urls')),
    # path("authentication/", include('authentication.urls')),
    # path("another_app/", include('another_app.urls'))
]

urlpatterns += staticfiles_urlpatterns()
