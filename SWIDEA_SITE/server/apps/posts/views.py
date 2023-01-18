from django.shortcuts import render, redirect
from .models import Post, Tool
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,JsonResponse
import json

# Create your views here.

def post_list(request):  
  sort = request.GET.get('sort','')
  if sort == 'pk':
    post_li = Post.objects.all().order_by("pk")
  elif sort == 'title':
    post_li = Post.objects.all().order_by("title")
  elif sort == 'new':
    post_li = Post.objects.all().order_by("-pk")
  elif sort == 'like':
    post_li = Post.objects.all().order_by("like_users")
  else:
    post_li = Post.objects.all()
    
  page = request.GET.get('page', 1)
  paginator = Paginator(post_li, 4)
  
  try:
    posts = paginator.page(page)
  except PageNotAnInteger:
    posts = paginator.page(1)
  except EmptyPage:
    posts = paginator.page(paginator.num_pages)

  context = {
    "posts" : posts,
  }
  return render(request, 'posts/post_list.html', context=context)

def post_detail(request, pk):
  post = Post.objects.get(pk=pk)
  tool_pk = post.devtool.pk
  context = {
    "post" : post,
    "tool_pk" : tool_pk,
  }
  return render(request, 'posts/post_detail.html', context=context)

def tool_list(request):
  tool_li = Tool.objects.all()
  page = request.GET.get('page', 1)
  paginator = Paginator(tool_li, 6)
  try:
    tools = paginator.page(page)
  except PageNotAnInteger:
    tools = paginator.page(1)
  except EmptyPage:
    tools = paginator.page(paginator.num_pages)
  context = {
    "tools" : tools,
  }
  return render(request, 'posts/tool_list.html', context=context)

def tool_detail(request, pk):
  tool = Tool.objects.get(pk=pk)
  post = Post.objects.all()
  tool_posts = Post.objects.filter(devtool=tool.id)
  context = {
    "tool" : tool,
    "tool_posts" : tool_posts,
  }
  return render(request, 'posts/tool_detail.html', context=context)

# def post_create(request, *args, **kwargs):
#   if request.method == "POST":
#     Post.objects.create(
#       title=request.POST["title"],
#       image=request.FILES["image"],
#       content=request.POST["content"],
#       interest=request.POST["interest"],
#       devtool=request.POST["devtool"],
#     )
#     return redirect("/")
#   return render(request, "posts/post_create.html")

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
  model = Post
  fields = ['title', 'image', 'content', 'interest', 'devtool']
  template_name = 'posts/post_create.html'

  def test_func(self):
    return self.request.user.is_superuser or self.request.user.is_staff

  def form_valid(self, form):
    current_user = self.request.user

    if current_user.is_authenticated and (current_user.is_superuser or current_user.is_staff):
      return super(PostCreate, self).form_valid(form)
    else:
      return redirect('/')
  
class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  fields = ['title', 'image', 'content', 'interest', 'devtool']

  template_name = 'posts/post_update.html'

  def dispatch(self, request, *args, **kwargs):
    return super(PostUpdate, self).dispatch(request, *args, **kwargs)

def post_delete(request, pk):
  login_session = request.session.get('login_session', '')
  post = get_object_or_404(Post, id=pk)
  post.delete()
  return redirect('/')

class ToolCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
  model = Tool
  fields = ['name', 'kind', 'content']
  template_name = 'posts/tool_create.html'

  def test_func(self):
    return self.request.user.is_superuser or self.request.user.is_staff

  def form_valid(self, form):
    current_user = self.request.user

    if current_user.is_authenticated and (current_user.is_superuser or current_user.is_staff):
      return super(ToolCreate, self).form_valid(form)
    else:
      return redirect('/tool/')
    
class ToolUpdate(LoginRequiredMixin, UpdateView):
  model = Tool
  fields = ['name', 'kind', 'content']

  template_name = 'posts/tool_update.html'

  def dispatch(self, request, *args, **kwargs):
    return super(ToolUpdate, self).dispatch(request, *args, **kwargs)

def tool_delete(request, pk):
  login_session = request.session.get('login_session', '')
  tool = get_object_or_404(Tool, id=pk)
  tool.delete()
  return redirect('/tool/')

def post_like(request, post_id):
  response_body = {"result": ""}

  if request.user.is_authenticated:
    if request.method == "POST":
      post = get_object_or_404(Post, pk=post_id)
      existed_user = post.likes.filter(pk=request.user.id).exists()

      if existed_user:
        post.likes.remove(request.user)
        response_body["result"] = "dislike"

      else:
        post.likes.add(request.user)
        response_body["result"] = "like"

      post.save()
      return JsonResponse(status=200, data=response_body)

  else:
      return JsonResponse(status=403, data=response_body)

def likes(request, post_pk):
  if request.user.is_authenticated:
    post = get_object_or_404(Post, pk=post_pk)

    if post.like_users.filter(pk=request.user.pk).exists():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('posts:list')
  return redirect('/')

# def like_post(request, pk):
  # if request.is_ajax(): #ajax 방식일 때 아래 코드 실행
  #   blog_id = request.GET['post.pk'] #좋아요를 누른 게시물id (blog_id)가지고 오기
  #   post = Blogapp.objects.get(id=blog_id) 
    
  #   if not request.user.is_authenticated: #버튼을 누른 유저가 비로그인 유저일 때
  #       message = "로그인을 해주세요" #화면에 띄울 메세지 
  #       context = {'like_count' : post.like.count(),"message":message}
  #       return HttpResponse(json.dumps(context), content_type='application/json')

  #   user = request.user #request.user : 현재 로그인한 유저
  #   if post.like.filter(id = user.id).exists(): #이미 좋아요를 누른 유저일 때
  #       post.like.remove(user) #like field에 현재 유저 추가
  #       message = "좋아요 취소" #화면에 띄울 메세지
  #   else: #좋아요를 누르지 않은 유저일 때
  #       post.like.add(user) #like field에 현재 유저 삭제
  #       message = "좋아요" #화면에 띄울 메세지
  #   context = {'like_count' : post.like.count(),"message":message}
    
  #   return HttpResponse(json.dumps(context), content_type='application/json')   
  