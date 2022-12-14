from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import redirect

class Post_List(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.order_by("-creation_date")
        form = PostForm()

        context = {
            "post_list" : posts,
            "form" : form,
        }

        return render(request, 'social/post_list.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.order_by('-creation_date')
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.creator = request.user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,
        }
        return redirect('/feed')


class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(parent_post=post).order_by('-comment_date')
        context = {
            "post" : post,
            "form" : form,
            'comments' : comments,
        }
        return render(request, 'social/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)
        comments = Comment.objects.filter(parent_post=post).order_by('-comment_date')
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.creator = request.user
            new_comment.parent_post = post
            new_comment.save()

            comments = Comment.objects.filter(parent_post=post).order_by('-comment_date')
            context = {
                "post": post,
                "form": form,
                'comments': comments,
            }
            return redirect(f'/feed/post/{pk}')
        return render(request, 'social/post_detail.html',
                      {"post": post,
                        "form": form,
                        'comments': comments,
                       })

class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'social/post_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk' : pk})

    def test_func(self):
        post= self.get_object()
        if self.request.user.is_staff:
            return True
        return self.request.user == post.creator

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'social/post_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_staff:
            return True
        return self.request.user == post.creator

class CommentEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['comment', 'rating']
    template_name = 'social/comment_edit.html'

    def get_success_url(self):
        pk = self.kwargs["post_pk"]
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        comment = self.get_object()
        if self.request.user.is_staff:
            return True
        return self.request.user == comment.creator


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'social/comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs["post_pk"]
        return reverse_lazy('post-detail', kwargs={'pk' : pk})

    def test_func(self):
        comment = self.get_object()
        if self.request.user.is_staff:
            return True
        return self.request.user == comment.creator

class SupportListView(LoginRequiredMixin, View):
    pass