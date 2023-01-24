from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
  path('', views.post_list, name='list'),
  path('like_ajax/', views.like_ajax, name='like'),
  path('post_new/', views.PostCreate.as_view(), name='post_new'),
  path('comment/', views.comment_ajax, name='comment'),
  path('comment/delete/', views.delete_comment, name='delete_comment'),
]
