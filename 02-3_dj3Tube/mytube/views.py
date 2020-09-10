from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Video, Comment
from .forms import VideoForm, CommentForm
from django.urls import reverse_lazy
from django.shortcuts import resolve_url, get_object_or_404

# https://docs.djangoproject.com/en/3.1/topics/auth/default/
# Limiting access to logged-in users that pass a test Custom Mixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import F


# Create your views here.
class VideoListView(ListView):
    model = Video
    template_name = "mytube/list.html"
    paginate_by = 3

    # Object List View QuerySet
    def get_queryset(self):

        print(self.kwargs)
        querySet = super().get_queryset()
        q = self.request.GET.get("q", "").strip()
        if q:
            querySet = querySet.filter(title__icontains=q)
        return querySet


class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    form_class = VideoForm
    template_name = "form.html"

    def form_valid(self, form):
        video = form.save(commit=False)
        video.author = self.request.user
        return super().form_valid(form)


class VideoDetailView(DetailView):
    model = Video
    template_name = "mytube/detail.html"

    # Counting the Video View Counts
    # get_object() : ORM Object Setter Function.
    def get_object(self, queryset=None):

        for k, v in self.kwargs.items():
            print(f"key:{k}/tvalue:{v}")

        pk = self.kwargs["pk"]

        # `F` is Captualization of Query Expression
        Video.objects.filter(pk=pk).update(view_count=F("view_count") + 1)
        return super().get_object(queryset=queryset)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["comment_form"] = CommentForm()
        return context_data


class VideoUpdateView(UserPassesTestMixin, UpdateView):
    model = Video
    form_class = VideoForm
    template_name = "form.html"

    def test_func(self):
        return self.request.user == self.get_object().author


class VideoDeleteView(UserPassesTestMixin, DeleteView):
    model = Video
    template_name = "mytube/delete_confirm.html"
    success_url = reverse_lazy("mytube:list")

    def test_func(self):
        return self.request.user == self.get_object().author


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "form.html"

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.video = get_object_or_404(
            Video, pk=self.kwargs["video_pk"]
        )  # url 'arg' name
        return super().form_valid(form)

    def get_success_url(self):
        return resolve_url("mytube:detail", self.kwargs["video_pk"])


class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        return self.request.user == self.get_object().author

    # `resolve_url()` is better than `reverse()`
    # https://wayhome25.github.io/django/2017/05/05/django-url-reverse/`
    def get_success_url(self):
        return resolve_url("mytube:detail", self.kwargs["video_pk"])
