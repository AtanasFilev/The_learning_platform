# Generated by Django 4.1.4 on 2022-12-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0009_alter_post_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='document',
            field=models.FileField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]