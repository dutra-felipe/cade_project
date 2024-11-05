from django.contrib import admin
from django.utils import timezone
from .models import Contato, Newsletter

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'tipo_requisicao', 'inscrito_newsletter', 'data_envio')
    list_filter = ('tipo_requisicao', 'inscrito_newsletter', 'data_envio')
    search_fields = ('nome', 'sobrenome', 'email', 'mensagem')
    readonly_fields = ('data_envio',)

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao', 'enviada', 'data_envio')
    list_filter = ('enviada', 'data_envio')
    search_fields = ('titulo', 'conteudo')
    readonly_fields = ('data_criacao', 'data_envio', 'enviada')
    actions = ['enviar_newsletter']

    def enviar_newsletter(self, request, queryset):
        for newsletter in queryset:
            if not newsletter.enviada:
                newsletter.enviar_newsletter()
                newsletter.enviada = True
                newsletter.data_envio = timezone.now()
                newsletter.save()
                self.message_user(request, f'Newsletter "{newsletter.titulo}" enviada com sucesso!')
            else:
                self.message_user(request, f'Newsletter "{newsletter.titulo}" já foi enviada anteriormente.', level='WARNING')
    
    enviar_newsletter.short_description = "Enviar newsletters selecionadas"