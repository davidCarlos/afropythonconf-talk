from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("create_v1", views.create_without_signal_v1, name="create_v1"),
    path("create_v2", views.create_without_signal_v2, name="create_v2"),
    path("create_v3", views.create_with_signal, name="create_v3"),
    path("detail_v1/<int:post_id>", views.detail_without_middleware, name="detail_v1"),
    path("detail_v2/<int:post_id>", views.detail_middleware, name="detail_v2"),
    path("create_without_decorator", views.create_without_decorator, name="create_v4"),
    path("create_with_decorator", views.create_with_decorator, name="create_v5"),
]
