from django.urls import path
from . import views

urlpatterns = [
  path('', views.reviews_list, name='reviews'),
  path('review/<int:pk>/', views.reviews_detail),
  path('review/<int:pk>/delete/', views.reviews_delete),
  path('review/create/', views.ReviewCreate.as_view()),
  path('review/edit/<int:pk>/', views.ReviewEdit.as_view()),
]