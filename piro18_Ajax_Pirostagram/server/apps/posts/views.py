from django.shortcuts import render
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

def post_list(request, *args, **kwargs):
  posts = Post.objects.all()
  context = {
    "posts" : posts,
  }
  return render(request, 'posts/post_list.html', context=context)

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
  model = Post
  fields = ['user', 'image', 'content', 'local', 'likes']
  template_name = 'posts/post_create.html'

  def test_func(self):
    return self.request.user.is_superuser or self.request.user.is_staff

  def form_valid(self, form):
    current_user = self.request.user

    if current_user.is_authenticated and (current_user.is_superuser or current_user.is_staff):
      return super(PostCreate, self).form_valid(form)
    else:
      return redirect('/')

@login_required
@csrf_exempt
def like_ajax(request, *args, **kwargs):
  data = json.loads(request.body)
  post_id = data['id']
  post = Post.objects.get(id=post_id)
  
  if post.likes == True: 
    post.likes = False
    status = data['type']
  else:
    post.likes = True
    status = data['type']
    
  post.save()
  content = {
    'id' : post_id,
    'status' : status,
  }
  return JsonResponse(content)


@csrf_exempt
def comment_ajax(request, *args, **kwargs):
  data = json.loads(request.body)
  post = Post.objects.get(id=data["post_id"])
  comment = Comment.objects.create(
    post = post,
    author = request.user,
    content = data.get('content'),
  )
  
  comment.save()
  
  content = {
    'author' : str(comment.author),
    'post_id' : post.id,
    'content' : comment.content,
    'comment_id' : comment.id,
  }
  
  return JsonResponse(content)

@csrf_exempt
def delete_comment(request, *args, **kwargs):
  data = json.loads(request.body)
  Comment.objects.get(id=data["comment_id"]).delete()
  content = {
    'comment_id' : data.get('comment_id'),
  }
  return JsonResponse(content)