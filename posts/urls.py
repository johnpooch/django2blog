from django.urls import path
from posts.views import get_posts, my_posts, post_detail, create_or_edit_post

urlpatterns = [
    path('new/', create_or_edit_post, name='new_post'),
    path('<pk>/edit', create_or_edit_post, name='edit_post'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('myposts/', my_posts, name='my_posts'),
    path('', get_posts, name='get_posts'),
]
