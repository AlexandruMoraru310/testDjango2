from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.published.all()
    print(type(posts))
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED)
    print(type(post.publish))
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
