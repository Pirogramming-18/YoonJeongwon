from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel

# Create your models here.

class Tool(models.Model):
  name = models.CharField(max_length=30, verbose_name= '이름')
  kind = models.CharField(max_length=30, verbose_name= '종류')
  content = models.TextField(verbose_name= '개발툴 설명')

  def __str__(self):
    return self.name
    
  def get_absolute_url(self):
    return f'/tool/{self.pk}/'
  

class Post(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', null=True)
  title = models.CharField(max_length=30, verbose_name= '아이디어명')
  image = models.ImageField(upload_to="posts/%Y%m%d", verbose_name='Image')
  content = models.TextField(verbose_name='아이디어 설명')
  interest = models.IntegerField(default=0,verbose_name='아이디어 관심도')
  devtool = models.ForeignKey(Tool, null=True, on_delete=models.SET_NULL, related_name="post_user",verbose_name='예상 개발툴')
  
  # custom_panels = [
  #           MultiFieldPanel([
  #               FieldRowPanel([
  #                   FieldPanel('first_name', classname='fn'),
  #                   FieldPanel('last_name', classname='ln'),
  #               ]),
  #               FieldPanel('address', classname='custom1',)
  #           ])
  #       ]
  # edit_handler = ObjectList(custom_panels)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return f'/post/{self.pk}/'
  
  def total_likes(self):
    return self.likes.count()