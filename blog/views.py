from .models import Post
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404

# from django.shortcuts import render, get_object_or_404
# from .forms import PostForm
# from django.shortcuts import redirect
# from django.shortcuts import render


# Create your views here.
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        q = super(PostListView, self).get_queryset()
        return q.filter(published_date__lte=timezone.now()).order_by(
            '-published_date')


class PostDetailVew(DetailView):
    model = Post
    context_object_name = 'post'


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('name_post_list')

    def dispatch(self, *args, **kwargs):
        return super(DeletePostView, self).dispatch(*args, **kwargs)

class CreatePostView(CreateView):
    model = Post
    fields = ['title', 'text']
    template_name = "blog/post_edit.html"

    def get_success_url(self):
        pk = self.object.pk
        return reverse_lazy('name_post_detail', kwargs={"pk": pk})

    def form_valid(self, form):
        form.instance.published_date = timezone.now()
        form.instance.author = self.request.user
        return super(CreatePostView, self).form_valid(form)


class UpdatePostView(UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = "blog/post_edit.html"

    def form_valid(self, form):
        form.instance.published_date = timezone.now()
        form.instance.author = self.request.user
        pk = form.instance.pk
        self.success_url = reverse_lazy('name_post_detail', kwargs={"pk": pk})

        return super(UpdatePostView, self).form_valid(form)

# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('name_post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
#         'published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})


# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})

#def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('name_post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})