from django.urls import path
from fb_post import views


urlpatterns = [
    path('post/', views.get_create_post_view),
    path('post/<int:post_id>/', views.get_post_view),
    path('comment/<int:comment_id>/reply/create/', views.get_reply_to_comment_view),
    path('post/<int:post_id>/react/', views.get_react_to_post_view),
    path('comment/<int:comment_id>/react/', views.get_react_to_comment_view),
    path('post/<int:post_id>/delete/', views.get_delete_post_view),
    path('post/<int:post_id>/comment/create/', views.get_create_comment_view)
]