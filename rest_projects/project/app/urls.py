from django.urls import path
from app import views


urlpatterns = [
    path('user/<int:user_id>/', views.get_posts_view),
    # path('user/<int:user_id>/create/post', views.get_create_post_view)
]
