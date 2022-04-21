from django.shortcuts import render
from django.core.mail import send_mail

from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def create(request):
    post = Post(title="primeiro post", body="esse é o primeiro post do nosso blog")
    post.save()
    return render(request, 'blog/create.html', {'post': post})

def create_without_signal_v1(request):
    post = Post(title="primeiro post", body="esse é o primeiro post do nosso blog")
    post.save()
    send_mail(
        'Um novo post foi criado',
        f'Título do post: {post.title}',
        'davidcarlos@pencillabs.com.br',
        ['g1@globo.com'],
        fail_silently=True,
    )
    return render(request, 'blog/create.html', {'post': post})

def create_without_signal_v2(request):
    from .helper import MailerHelper

    post = Post(title="primeiro post", body="esse é o primeiro post do nosso blog")
    post.save()
    MailerHelper(post).send()
    return render(request, 'blog/create.html', {'post': post})

def create_with_signal(request):
    post = Post(title="primeiro post", body="esse é o primeiro post do nosso blog")
    post.save()
    return render(request, 'blog/create.html', {'post': post})
