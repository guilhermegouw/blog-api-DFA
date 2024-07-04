from django.contrib import admin
from django.urls import include, path

from accounts.views import CustomLoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("posts.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/login/", CustomLoginView.as_view(), name="custom_login"),
]
