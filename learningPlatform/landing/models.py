from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    title = models.TextField(default="no title")
    body = models.TextField(default="no body")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
