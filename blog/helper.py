from dataclasses import dataclass
from django.core.mail import send_mail


@dataclass
class MailerHelper:
    post_title: str

    def send(self):
        send_mail(
            "Um novo post foi criado",
            f"Título do post: {self.post_title}",
            "davidcarlos@pencillabs.com.br",
            ["g1@globo.com"],
            fail_silently=True,
        )


class DollarHelper:
    @staticmethod
    def get_dollar_today():
        # acessa alguma API remota para recuperar a cotação do dolar
        return 9

class IdValidatorHelper:
    @staticmethod
    def validate(id):
        # alguma regra maluca de validação
        return id and int(id) > 100
