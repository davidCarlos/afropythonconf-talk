from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from blog.models import Post


@receiver(post_save, sender=Post)
def send_email_callback(sender, **kwargs):
    post = kwargs.get("instance")
    print(post.title)
    send_mail(
        "Um novo post foi criado",
        f"Título do post: {post.title}",
        "davidcarlos@pencillabs.com.br",
        ["g1@globo.com"],
        fail_silently=True,
    )
