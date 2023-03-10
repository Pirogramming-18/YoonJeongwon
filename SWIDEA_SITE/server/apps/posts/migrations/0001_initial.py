# Generated by Django 4.1.5 on 2023-01-17 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('kind', models.CharField(max_length=30)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='posts/%Y%m%d')),
                ('content', models.TextField()),
                ('interest', models.IntegerField(default=0)),
                ('devtool', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_user', to='posts.tool')),
            ],
        ),
    ]
