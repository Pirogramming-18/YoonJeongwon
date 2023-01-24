from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='posts/%Y%m%d')
  content = models.TextField()
  local = models.CharField(max_length=20, null=True, blank=True)
  likes = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f'[{self.pk}]{self.content}'
  
  def get_absolute_url(self):
    return f'/'
  
class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  
  def __str__(self):
    return f'{self.post}, {self.author}'