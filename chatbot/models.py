from django.db import models
from django.utils.translation import gettext_lazy as _


class FAQCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('FAQ Category')
        verbose_name_plural = _('FAQ Categories')


class FAQ(models.Model):
    category = models.ForeignKey('FAQCategory', on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    language = models.CharField(max_length=2, choices=[
        ('pt', 'Portuguese'),
        ('en', 'English'),
        ('es', 'Spanish')
    ])
    is_predefined = models.BooleanField(default=False)  # Novo campo
    order = models.IntegerField(default=0)  # Para controlar a ordem de exibição

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')
        ordering = ['order', 'question']  # Ordenar por ordem e depois por questão

    def __str__(self):
        return self.question


class SearchKeyword(models.Model):
    keyword = models.CharField(max_length=100)
    normalized_term = models.CharField(max_length=100)
    language = models.CharField(max_length=2)

    class Meta:
        verbose_name = _('Search Keyword')
        verbose_name_plural = _('Search Keywords')


class ChatMessage(models.Model):
    user_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=2)
    was_helpful = models.BooleanField(null=True)
