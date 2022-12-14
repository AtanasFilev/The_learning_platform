# Generated by Django 4.1.4 on 2022-12-12 17:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_rename_comment_time_post_creation_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='creation_time',
        ),
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
