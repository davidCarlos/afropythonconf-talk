from blog.decorators import user_has_valid_id
from blog.helper import IdValidatorHelper
from django.shortcuts import render
from django.core.mail import send_mail

from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html", {"posts": posts})


def detail_without_middleware(request, post_id):
    from .helper import DollarHelper

    post = Post.objects.get(id=post_id)
    return render(
        request,
        "blog/detail.html",
        {"post": post, "dollar_today": DollarHelper.get_dollar_today()},
    )


def detail_middleware(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "blog/detail_middleware.html", {"post": post})

def create(request):
    post = Post(title="primeiro post", body="esse é o primeiro post do nosso blog")
    post.save()
    return render(request, "blog/create.html", {"post": post})


def create_without_signal_v1(request):
    post = Post(title="primeiro post", body="esse é o primeiro post do nosso blog")
    post.save()
    send_mail(
        "Um novo post foi criado",
        f"Título do post: {post.title}",
        "davidcarlos@pencillabs.com.br",
        ["g1@globo.com"],
        fail_silently=True,
    )
    return render(request, "blog/create.html", {"post": post})


def create_without_signal_v2(request):
    from .helper import MailerHelper

    post = Post(title="primeiro post", body="esse é o primeiro post do nosso blog")
    post.save()
    MailerHelper(post).send()
    return render(request, "blog/create.html", {"post": post})


def create_with_signal(request):
    post = Post(title="primeiro post", body="esse é o primeiro post do nosso blog")
    post.save()
    return render(request, "blog/create.html", {"post": post})

def create_without_decorator(request):
    unique_id = request.GET.get('id')
    if IdValidatorHelper.validate(unique_id):
        post = Post(title="primeiro post", body="esse é o primeiro post do nosso blog")
        post.save()
        return render(request, "blog/create.html", {"post": post})
    return render(request, "blog/invalid_id_error.html")

@user_has_valid_id
def create_with_decorator(request):
    post = Post(title="primeiro post", body="esse é o primeiro post do nosso blog")
    post.save()
    return render(request, "blog/create.html", {"post": post})
