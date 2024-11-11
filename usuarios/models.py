from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


class Contato(models.Model):
    TIPO_REQUISICAO_CHOICES = [
        ('contato', 'Contatar CADE'),
        ('newsletter', 'Assinar Newsletter'),
        ('ambos', 'Contatar CADE e Assinar Newsletter'),
    ]

    tipo_requisicao = models.CharField(
        max_length=20,
        choices=TIPO_REQUISICAO_CHOICES,
        default='contato'
    )
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    cargo = models.CharField(max_length=100)
    mensagem = models.TextField(blank=True, null=True)
    data_envio = models.DateTimeField(auto_now_add=True)
    inscrito_newsletter = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return f"{self.nome} {self.sobrenome} - {self.get_tipo_requisicao_display()}"

    def save(self, *args, **kwargs):
        # Verifica se é um novo registro
        is_new = self.pk is None

        # Define se deve receber newsletter baseado no tipo de requisição
        if self.tipo_requisicao in ['newsletter', 'ambos']:
            self.inscrito_newsletter = True

        super().save(*args, **kwargs)

        # Se for novo registro e inscrito na newsletter, envia email de boas-vindas
        if is_new and self.inscrito_newsletter:
            self.enviar_email_boasvindas()

    def enviar_email_boasvindas(self):
        subject = 'Bem-vindo à Newsletter do CADE'

        html_message = render_to_string('newsletter.html', {
            'nome': self.nome,
            'email': self.email
        })

        plain_message = strip_tags(html_message)

        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [self.email],
            html_message=html_message,
            fail_silently=False,
        )


class Newsletter(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_envio = models.DateTimeField(null=True, blank=True)
    enviada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    def enviar_newsletter(self):
        inscritos = Contato.objects.filter(inscrito_newsletter=True)

        for inscrito in inscritos:
            html_message = render_to_string('newsletter.html', {
                'nome': inscrito.nome,
                'titulo': self.titulo,
                'conteudo': self.conteudo,
                'email': inscrito.email
            })

            plain_message = strip_tags(html_message)

            send_mail(
                f'Newsletter CADE - {self.titulo}',
                plain_message,
                settings.DEFAULT_FROM_EMAIL,
                [inscrito.email],
                html_message=html_message,
                fail_silently=False,
            )
