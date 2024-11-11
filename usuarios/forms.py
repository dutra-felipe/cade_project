from django import forms
from .models import Contato, Newsletter


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['tipo_requisicao', 'nome', 'sobrenome', 'email', 'cargo', 'mensagem']
        widgets = {
            'tipo_requisicao': forms.RadioSelect,
            'mensagem': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'tipo_requisicao': 'Como podemos ajudar?',
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'email': 'E-mail',
            'cargo': 'Cargo',
            'mensagem': 'Mensagem',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'tipo_requisicao':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': self.fields[field].label
                })


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['titulo', 'conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 10}),
        }
