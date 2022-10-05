# Generated by Django 4.1.1 on 2022-10-05 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_project', '0003_alter_project_custom_tag_alter_project_title_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='custom_tag',
            field=models.CharField(max_length=300),
        ),
        migrations.AddField(
            model_name='project',
            name='custom_tag_set',
            field=models.ManyToManyField(blank=True, to='search_project.customtag'),
        ),
    ]
