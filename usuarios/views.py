from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import ContatoForm


def index(request):
    return render(request, 'index.html')


class ContatoView(TemplateView):
    template_name = 'contato.html'


class EventosView(TemplateView):
    template_name = 'eventos.html'


class NotasView(TemplateView):
    template_name = 'notas.html'


class NovidadesView(TemplateView):
    template_name = 'novidades.html'


class SobreView(TemplateView):
    template_name = 'sobre.html'


class CasosRecentesView(TemplateView):
    template_name = 'casos.html'


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('contato')
    else:
        form = ContatoForm()

    return render(request, 'contato.html', {'form': form})
