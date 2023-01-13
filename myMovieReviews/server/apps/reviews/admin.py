from django.contrib import admin
from .models import Review, Category, Actor

# Register your models here.

admin.site.register(Review)

class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ActorAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}
admin.site.register(Actor, ActorAdmin)