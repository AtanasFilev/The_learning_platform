from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.conf import settings

class Post(models.Model):
    title = models.TextField(default="no title")
    body = models.TextField(default="no body")
    creation_date = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField(upload_to="uploads/", null=True, blank=True)

class Comment(models.Model):
    comment = models.TextField(validators=[MinLengthValidator(3)], default="no comment")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=0)
    comment_date = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_post = models.ForeignKey('Post', on_delete=models.CASCADE)

class Support_ticket(models.Model):
    issue = models.TextField(default="no title")
    description = models.TextField(default="no body")
    creation_date = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class Response(models.Model):
    response = models.TextField(validators=[MinLengthValidator(3)], default="no comment")
    comment_date = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_post = models.ForeignKey('Support_ticket', on_delete=models.CASCADE)
