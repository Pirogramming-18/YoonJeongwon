from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=16, unique=True)
  slug = models.SlugField(max_length=16, unique=True, allow_unicode=True)

  def __str__(self):
    return self.name

class Actor(models.Model):
  name = models.CharField(max_length=50, unique=True)
  slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

  def __str__(self):
    return self.name

class Review(models.Model):
  title = models.CharField(max_length=32)
  year = models.IntegerField(default=2000)
  image = models.ImageField(upload_to='reviews/images/%Y/%m/%d', blank=True)

  category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
  star = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
  time = models.IntegerField()
  review = models.TextField()
  
  director = models.CharField(max_length=16)
  actor = models.ManyToManyField(Actor, blank=True)

  # author = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return f'/review/{self.pk}/'
  