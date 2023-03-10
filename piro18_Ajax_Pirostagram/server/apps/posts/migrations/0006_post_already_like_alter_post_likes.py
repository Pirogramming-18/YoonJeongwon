# Generated by Django 4.1.5 on 2023-01-24 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_likes_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='already_like',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.TextField(default='<i class="far fa-heart"></i> '),
        ),
    ]
