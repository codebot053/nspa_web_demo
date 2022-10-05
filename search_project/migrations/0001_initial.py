# Generated by Django 4.1.1 on 2022-10-04 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DevTechnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='기술 스택')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=500)),
                ('location', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('technology_tag', models.ManyToManyField(blank=True, to='search_project.devtechnology')),
            ],
        ),
    ]