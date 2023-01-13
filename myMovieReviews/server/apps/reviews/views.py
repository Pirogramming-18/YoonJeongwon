from django.shortcuts import render, redirect
from .models import Review
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
# Create your views here.


def reviews_list(request):
  sort = request.GET.get('sort','')
  
  if sort == 'title':
    reviews = Review.objects.all().order_by("title")
  elif sort == 'star':
    reviews = Review.objects.all().order_by("-star")
  elif sort == 'time':
    reviews = Review.objects.all().order_by("time")
  elif sort == 'pk':
    reviews = Review.objects.all().order_by("-pk")
  else:
    reviews = Review.objects.all()

  return render(request, "reviews/reviews_list.html", { 'reviews':reviews })

def reviews_detail(request, pk):
  review = Review.objects.get(pk=pk)
  hour = review.time // 60
  min = review.time % 60
  return render(request, "reviews/reviews_detail.html", { 'review':review ,
    'hour':hour, 'min':min })


class ReviewCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
  model = Review
  fields = ['title', 'year', 'image', 'category', 'star',
            'time', 'review', 'director', 'actor']

  template_name = 'reviews/reviews_create.html'

  success_url = '/'

  def test_func(self):
    return self.request.user.is_superuser or self.request.user.is_staff

  def form_valid(self, form):
    current_user = self.request.user

    if current_user.is_authenticated and (current_user.is_superuser or current_user.is_staff):
      return super(ReviewCreate, self).form_valid(form)
    else:
      return redirect('/')

class ReviewEdit(LoginRequiredMixin, UpdateView):
  model = Review
  fields = ['title', 'year', 'image', 'category', 'star',
            'time', 'review', 'director', 'actor']

  template_name = 'reviews/reviews_edit.html'

  def dispatch(self, request, *args, **kwargs):
    return super(ReviewEdit, self).dispatch(request, *args, **kwargs)

def reviews_delete(request, pk):
  login_session = request.session.get('login_session', '')
  review = get_object_or_404(Review, id=pk)
  review.delete()
  return redirect('/')
    