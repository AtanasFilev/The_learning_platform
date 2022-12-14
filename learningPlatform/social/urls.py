from django.urls import path
from .views import Post_List, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView, CommentEditView
from django.views.static import serve
from django.conf import settings


urlpatterns =[
    path("", Post_List.as_view(), name="post-list"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("post/edit/<int:pk>", PostEditView.as_view(), name="post-edit"),
    path("post/delete/<int:pk>", PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:post_pk>/comment/edit/<int:pk>", CommentEditView.as_view(), name="comment-edit"),
    path("post/<int:post_pk>/comment/delete/<int:pk>", CommentDeleteView.as_view(), name="comment-delete"),
    path('download/<path:path>', serve, {'document_root': str(settings.MEDIA_ROOT)}, name="download"),
]