from django.contrib import admin
from .models import Post, Comment, Support_ticket



admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Support_ticket)

# Register your models here.
