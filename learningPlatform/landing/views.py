from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Review
from .forms import ReviewForm
class Index(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_staff:
            return redirect("post-list")
        return render(request, 'landing/index.html')

class Review_List(View):
    def get(self, request, *args, **kwargs):
        posts = Review.objects.order_by("-rating")
        form = ReviewForm()

        context = {
            "reviews" : posts,
            "form" : form,
        }

        return render(request, 'landing/about _us.html', context)

    def post(self, request, *args, **kwargs):
        posts = Review.objects.order_by("-rating")
        form = ReviewForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.creator = request.user
            new_post.save()

        context = {
            'reviews': posts,
            'form': form,
        }
        return redirect('/about')