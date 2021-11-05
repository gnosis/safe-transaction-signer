from django.contrib import admin
from django.urls import path, include

url_patterns_v1 = [
    path("transactions/", include("submit_signature.urls", namespace="transactions"))
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include((url_patterns_v1, "v1"), namespace="v1")),
]
