# Generated by Django 4.2 on 2023-04-20 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_bookmark_like_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='like_count',
        ),
    ]
