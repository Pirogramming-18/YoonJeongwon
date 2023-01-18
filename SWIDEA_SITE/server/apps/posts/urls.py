from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
  path('', views.post_list, name='list'),
  path('post/<int:pk>/', views.post_detail, name='detail'),
  path('post/create/', views.PostCreate.as_view(), name='create'),
  path('post/update/<int:pk>/', views.PostUpdate.as_view(), name='update'),
  path('post/delete/<int:pk>/', views.post_delete, name='delete'),
  path('tool/', views.tool_list, name='tool_list'),
  path('tool/<int:pk>/', views.tool_detail, name='tool_detail'),
  path('tool/create/', views.ToolCreate.as_view(), name='tool_create'),
  path('tool/update/<int:pk>/', views.ToolUpdate.as_view(), name='tool_update'),
  path('tool/delete/<int:pk>/', views.tool_delete, name='tool_delete'),
  path('post/like/<int:post_pk>/', views.likes, name='likes'),
]